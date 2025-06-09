from helpers.bootstrap.verify import verify_tool, verify_venv
import importlib
import os
import subprocess
from pathlib import Path
from typing import Any

import helpers.tools.python as pytools

dx = importlib.import_module("helpers.bootstrap.40_dx")
verify_pre_commit_hooks = dx.verify_pre_commit_hooks
venv_environment = dx.venv_environment


def test_verify_tool_python():
  res = verify_tool("python")
  assert res["installed"]
  assert res["version"] is not None


def test_verify_tool_missing():
  res = verify_tool("unlikely_tool")
  assert not res["installed"]


def test_verify_venv(tmp_path):
  venv_path = tmp_path / "env"
  import venv

  venv.EnvBuilder(with_pip=True).create(venv_path)

  res = verify_venv(venv_path)
  assert res["valid"]
  assert not res["corrupt"]


def test_verify_venv_corrupt(tmp_path):
  venv_path = tmp_path / "env"
  venv_path.mkdir()
  (venv_path / "pyvenv.cfg").write_text("# fake")
  res = verify_venv(venv_path)
  assert not res["valid"]
  assert res["corrupt"]


def test_verify_pre_commit_hooks(tmp_path):
  hooks = tmp_path / ".git" / "hooks"
  hooks.mkdir(parents=True)
  (hooks / "pre-commit").write_text("echo")
  res = verify_pre_commit_hooks(tmp_path)
  assert res["pre_commit"]["installed"]


def test_venv_environment_sets_path(tmp_path):
  env = venv_environment(tmp_path)
  assert env["VIRTUAL_ENV"] == str(tmp_path)
  assert str(tmp_path / "bin") in env["PATH"].split(os.pathsep)[0]


def test_install_pre_commit_hooks_uses_venv(monkeypatch, tmp_path):
  calls: list[tuple[list[str], dict[str, Any]]] = []

  def fake_run(cmd, *args, **kwargs):
    calls.append((cmd, kwargs))
    return subprocess.CompletedProcess(cmd, 0)

  venv_path = tmp_path / "env"
  bin_dir = venv_path / "bin"
  bin_dir.mkdir(parents=True)

  monkeypatch.setattr(dx, "run_command", fake_run)
  monkeypatch.setattr(pytools, "resolve_venv_path", lambda name: Path("env"))

  res = dx.install_pre_commit_hooks(tmp_path)

  cmd, kwargs = calls[0]
  assert cmd == ["pre-commit", "--version"]
  assert kwargs["env"]["PATH"].split(os.pathsep)[0] == str(bin_dir)
  assert res["pre_commit"]["installed"]


def test_install_pre_commit_hooks_handles_missing(monkeypatch, tmp_path):
  def raise_fn(*args, **kwargs):
    raise FileNotFoundError

  monkeypatch.setattr(dx, "run_command", raise_fn)
  monkeypatch.setattr(pytools, "resolve_venv_path", lambda name: Path("env"))

  res = dx.install_pre_commit_hooks(tmp_path)

  assert not res["pre_commit"]["installed"]
  assert res["pre_commit"]["error"] == "pre-commit not found"
