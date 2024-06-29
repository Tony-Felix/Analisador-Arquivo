from datetime import date
import os
import pytest
from pro_filer.actions.main_actions import show_details  # NOQA


@pytest.mark.parametrize("context, output",
  [
    (
      {
        "base_path": "/home/trybe/????",
      },
      "File '????' does not exist\n",
    ),
  ],
)
def test_show_detail_file_dosent_exist(capsys, context, output):
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == output


def test_show_detail(tmp_path, capsys):
    tmp_file_path = tmp_path / "Trybe_logo.png"
    tmp_file_path.touch()

    file_path = {
      "base_path": str(tmp_file_path)
    }
   
    show_details(file_path)
    captured = capsys.readouterr()

    name = "Trybe_logo.png"
    size = os.path.getsize(str(tmp_file_path))
    type = "file"
    extension = ".png"
    result_date = date.fromtimestamp(os.path.getmtime(str(tmp_file_path)))

    assert captured.out == (
        f"File name: {name}\n"
        f"File size in bytes: {size}\n"
        f"File type: {type}\n"
        f"File extension: {extension}\n"
        f"Last modified date: {result_date}\n"
      )

def test_show_detail_without_extension(tmp_path, capsys):
    tmp_diretory_path = tmp_path / "diretorio"
    tmp_diretory_path.touch()

    show_details({
      "base_path": str(tmp_diretory_path)
    })

    captured = capsys.readouterr()

    name = "diretorio"
    size = os.path.getsize(str(tmp_diretory_path))
    type = "file"
    extension = "[no extension]"
    result_date = date.fromtimestamp(os.path.getmtime(str(tmp_diretory_path)))

    assert captured.out == (
      f"File name: {name}\n"
      f"File size in bytes: {size}\n"
      f"File type: {type}\n"
      f"File extension: {extension}\n"
      f"Last modified date: {result_date}\n"
    )