from __future__ import annotations

from pathlib import Path
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "quickstart.sh"


def run_quickstart(dest: Path, remote: str | None = None) -> None:
  env = os.environ.copy()
  env["QUICKSTART_TEMPLATE_REPO"] = str(ROOT)
  cmd = [str(SCRIPT), "-C", str(dest)]
  if remote:
    cmd += ["-u", remote]
  subprocess.run(cmd, check=True, env=env)


def test_quickstart_initializes_repo(tmp_path: Path) -> None:
  run_quickstart(tmp_path)
  result = subprocess.run(
    ["git", "-C", str(tmp_path), "rev-list", "--count", "HEAD"],
    capture_output=True,
    text=True,
    check=True,
  )
  assert result.stdout.strip() == "1"


def test_quickstart_configures_remote(tmp_path: Path) -> None:
  remote = "git@example.com:repo.git"
  run_quickstart(tmp_path, remote=remote)
  result = subprocess.run(
    ["git", "-C", str(tmp_path), "remote", "get-url", "origin"],
    capture_output=True,
    text=True,
    check=True,
  )
  assert result.stdout.strip() == remote
