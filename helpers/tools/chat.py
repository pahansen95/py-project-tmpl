"""Minimal chat client for Large Language Models."""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, List

from helpers.utils import HttpSession
from helpers.tools import tool, SubParser


class Role(str, Enum):
  """Conversation participant."""

  SYSTEM = "system"
  USER = "user"
  ASSISTANT = "assistant"


@dataclass
class TextPart:
  """Text content of a message."""

  text: str

  def to_dict(self) -> dict:
    return {"type": "text", "text": self.text}


@dataclass
class ImagePart:
  """Image content referenced by URL."""

  url: str
  detail: str | None = None

  def to_dict(self) -> dict:
    data = {"type": "image_url", "image_url": {"url": self.url}}
    if self.detail:
      data["image_url"]["detail"] = self.detail
    return data


Part = TextPart | ImagePart


@dataclass
class ChatMessage:
  """Single message in a chat conversation."""

  role: Role
  content: List[Part]

  def to_dict(self) -> dict:
    if len(self.content) == 1 and isinstance(self.content[0], TextPart):
      return {"role": self.role.value, "content": self.content[0].text}
    return {"role": self.role.value, "content": [p.to_dict() for p in self.content]}


class ChatClient:
  """Client for the OpenAI compatible chat API."""

  def __init__(self, base_url: str, api_key: str, model: str, *, timeout: float | None = None) -> None:
    self.base_url = base_url.rstrip("/")
    self.api_key = api_key
    self.model = model
    self.timeout = timeout

  def chat(self, messages: Iterable[ChatMessage]) -> str:
    """Send *messages* and return the assistant reply."""

    with HttpSession(self.base_url, timeout=self.timeout) as sess:
      payload = {
        "model": self.model,
        "messages": [m.to_dict() for m in messages],
      }
      body = json.dumps(payload)
      headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json",
      }
      with sess.post("/v1/chat/completions", body=body, headers=headers) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"]


class AzureChatClient(ChatClient):
  """Client for the Azure OpenAI chat API."""

  def __init__(
    self,
    base_url: str,
    api_key: str,
    deployment: str,
    *,
    api_version: str = "2023-05-15",
    timeout: float | None = None,
  ) -> None:
    super().__init__(base_url, api_key, deployment, timeout=timeout)
    self.api_version = api_version

  def chat(self, messages: Iterable[ChatMessage]) -> str:
    """Send *messages* and return the assistant reply."""

    with HttpSession(self.base_url, timeout=self.timeout) as sess:
      payload = {"messages": [m.to_dict() for m in messages]}
      body = json.dumps(payload)
      headers = {
        "api-key": self.api_key,
        "Content-Type": "application/json",
      }
      path = f"/openai/deployments/{self.model}/chat/completions?api-version={self.api_version}"
      with sess.post(path, body=body, headers=headers) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"]


class AnthropicChatClient(ChatClient):
  """Client for the Anthropic chat API."""

  def __init__(
    self,
    base_url: str,
    api_key: str,
    model: str,
    *,
    api_version: str = "2023-06-01",
    timeout: float | None = None,
  ) -> None:
    super().__init__(base_url, api_key, model, timeout=timeout)
    self.api_version = api_version

  def chat(self, messages: Iterable[ChatMessage]) -> str:
    """Send *messages* and return the assistant reply."""

    with HttpSession(self.base_url, timeout=self.timeout) as sess:
      payload = {
        "model": self.model,
        "messages": [m.to_dict() for m in messages],
      }
      body = json.dumps(payload)
      headers = {
        "x-api-key": self.api_key,
        "anthropic-version": self.api_version,
        "Content-Type": "application/json",
      }
      with sess.post("/v1/messages", body=body, headers=headers) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"]


class BedrockChatClient(ChatClient):
  """Client for the AWS Bedrock chat API."""

  def chat(self, messages: Iterable[ChatMessage]) -> str:
    """Send *messages* and return the assistant reply."""

    with HttpSession(self.base_url, timeout=self.timeout) as sess:
      payload = {"messages": [m.to_dict() for m in messages]}
      body = json.dumps(payload)
      headers = {
        "X-Amz-Bedrock-Api-Key": self.api_key,
        "Content-Type": "application/json",
      }
      path = f"/model/{self.model}/invoke"
      with sess.post(path, body=body, headers=headers) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"]


def _expand_env(value: object) -> object:
  """Recursively expand ``$VARNAME`` strings from the environment."""

  if isinstance(value, str) and value.startswith("$"):
    return os.environ.get(value[1:], "")
  if isinstance(value, dict):
    return {k: _expand_env(v) for k, v in value.items()}
  if isinstance(value, list):
    return [_expand_env(v) for v in value]
  return value


def load_config(path: str) -> dict:
  """Load JSON config from *path* and expand environment variables."""

  data = json.loads(Path(path).read_text())
  return _expand_env(data)  # type: ignore[return-value]


def create_client(cfg: dict) -> ChatClient:
  """Return chat client for configuration *cfg*.

  ``cfg['provider']`` should follow ``PROVIDER[:BACKEND]`` format using the
  names ``OpenAI``, ``OpenAI:Azure``, ``Anthropic``, or ``Anthropic:Bedrock``.
  ``BACKEND`` is optional and defaults to the public API.
  """

  provider = str(cfg.get("provider", "OpenAI"))
  main, _, backend = provider.partition(":")
  main = main.strip().lower()
  backend = backend.strip().lower() or None

  if main == "openai":
    if backend == "azure":
      return AzureChatClient(
        cfg["base_url"],
        cfg["api_key"],
        cfg["deployment"],
        api_version=cfg.get("api_version", "2023-05-15"),
        timeout=cfg.get("timeout"),
      )
    return ChatClient(
      cfg["base_url"],
      cfg["api_key"],
      cfg["model"],
      timeout=cfg.get("timeout"),
    )

  if main == "anthropic":
    if backend == "bedrock":
      return BedrockChatClient(
        cfg["base_url"],
        cfg["api_key"],
        cfg["model"],
        timeout=cfg.get("timeout"),
      )
    return AnthropicChatClient(
      cfg["base_url"],
      cfg["api_key"],
      cfg["model"],
      api_version=cfg.get("api_version", "2023-06-01"),
      timeout=cfg.get("timeout"),
    )

  raise ValueError(f"Unknown provider: {provider}")


def parse_fmt(fmt: str) -> tuple[str, str]:
  """Return ``(in_fmt, out_fmt)`` from *fmt* string."""

  if ":" in fmt:
    in_fmt, out_fmt = fmt.split(":", 1)
  else:
    in_fmt, out_fmt = fmt, "txt"

  if in_fmt not in {"txt", "log"} or out_fmt not in {"txt", "log"}:
    raise ValueError("fmt must use txt or log")
  return in_fmt, out_fmt


def parse_messages(data: str, fmt: str) -> list[ChatMessage]:
  """Parse *data* into messages according to *fmt*."""

  if fmt == "txt":
    text = data.strip()
    return [ChatMessage(Role.USER, [TextPart(text)])] if text else []

  messages: list[ChatMessage] = []
  for line in data.splitlines():
    if not line.strip():
      continue
    obj = json.loads(line)
    role = Role(obj["role"])
    content = obj["content"]
    if isinstance(content, str):
      messages.append(ChatMessage(role, [TextPart(content)]))
    else:
      parts: list[Part] = []
      for part in content:
        if part.get("type") == "text":
          parts.append(TextPart(part["text"]))
        elif part.get("type") == "image_url":
          img = part["image_url"]
          parts.append(ImagePart(img["url"], img.get("detail")))
      messages.append(ChatMessage(role, parts))
  return messages


def format_messages(messages: list[ChatMessage], fmt: str) -> str:
  """Serialize *messages* into *fmt*."""

  if fmt == "txt":
    last = messages[-1]
    if len(last.content) == 1 and isinstance(last.content[0], TextPart):
      return last.content[0].text
    return json.dumps(last.to_dict())

  return "\n".join(json.dumps(m.to_dict()) for m in messages)


def run(args: argparse.Namespace, *, in_stream=sys.stdin, out_stream=sys.stdout) -> None:
  """Run chat CLI."""

  in_fmt, out_fmt = parse_fmt(args.fmt)
  cfg = load_config(args.conf)
  prompt = Path(args.prompt).read_text() if args.prompt else None

  data = in_stream.read()
  messages = parse_messages(data, in_fmt)
  if prompt:
    messages.insert(0, ChatMessage(Role.SYSTEM, [TextPart(prompt.strip())]))

  client = create_client(cfg)
  reply = client.chat(messages)
  messages.append(ChatMessage(Role.ASSISTANT, [TextPart(reply)]))

  out_stream.write(format_messages(messages, out_fmt))
  if out_fmt == "log":
    out_stream.write("\n")


@tool("chat")
def register(subparsers: SubParser) -> None:
  parser = subparsers.add_parser("chat", help="Interact with a chat model")
  parser.add_argument("--fmt", default="txt:log", help="input[:output] format (txt or log)")
  parser.add_argument("-p", "--prompt", metavar="FILE", help="System prompt file")
  parser.add_argument("-c", "--conf", metavar="FILE", required=True, help="Model configuration file")
  parser.set_defaults(func=run)
