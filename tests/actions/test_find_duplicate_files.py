import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_empty_list(tmp_path):
  dir_1 = tmp_path / "dir1"
  dir_2 = tmp_path / "dir2"

  dir_1.mkdir()
  dir_2.mkdir()

  file_1 = dir_1 / "app.py"
  file_2 = dir_2 / "model.txt"
  file_2.touch()

  file_1.write_text("Coragem faz coragem")

  context = {"all_files": [str(file_1), str(file_2)]}

  result = find_duplicate_files(context)
  assert result == []


def test_find_duplicate(tmp_path):
  dir_1 = tmp_path / "dir1"
  dir_2 = tmp_path / "dir2"

  dir_1.mkdir()
  dir_2.mkdir()

  file_1 = dir_1 / "app.py"
  file_2 = dir_2 / "model.txt"

  file_1.write_text("Coragem faz coragem")
  file_2.write_text("Coragem faz coragem")

  context = {"all_files": [str(file_1), str(file_2)]}

  result = find_duplicate_files(context)
  assert result == [(str(file_1), str(file_2))]


def test_find_duplicate_error():
  context = {"all_files": ["src/app.py", "src/model.py"]}

  error_output = "All files must exist"
  with pytest.raises(ValueError, match=error_output):
    result = find_duplicate_files(context)