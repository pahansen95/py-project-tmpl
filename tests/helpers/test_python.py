from pathlib import Path
import argparse

import pytest

import helpers.tools.python as hp


def test_resolve_venv_path_default():
  assert hp.resolve_venv_path("default") == Path(".venv")


def test_resolve_venv_path_named():
  assert hp.resolve_venv_path("foo") == Path(".venv") / "foo"


def test_ensure_venv_exists(monkeypatch, tmp_path):
  monkeypatch.setattr(hp, "BASE_VENV_DIR", tmp_path / ".venv")
  existing = hp.BASE_VENV_DIR / "foo"
  existing.mkdir(parents=True)
  assert hp.ensure_venv_exists("foo") == existing
  with pytest.raises(SystemExit):
    hp.ensure_venv_exists("bar")


def test_deps_parser_includes_test_group() -> None:
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(dest="tool")
  hp.register(subparsers)
  python_parser = subparsers.choices["python"]
  action_subs = [a for a in python_parser._actions if isinstance(a, argparse._SubParsersAction)][0]
  deps_parser = action_subs.choices["deps"]
  group_action = [a for a in deps_parser._actions if getattr(a, "dest", None) == "group"][0]
  assert "test" in group_action.choices
