from helpers.bootstrap.verify import verify_tool, verify_venv


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
