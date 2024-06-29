import os
from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path  # NOQA


def test_show_disk_usage_falil(capsys):
    show_disk_usage({"all_files": []})
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage(capsys, tmp_path):
    diretory = tmp_path / "dir"
    diretory.mkdir()

    file_1 = diretory / "file_1.txt"
    file_1.write_text("Nonada. tiros que o senhor ouviu...")

    file_2 = diretory / "file_2.txt"
    file_2.write_text("o que existe é homem humano. Travessia..")

    dict_files = {"all_files": [str(file_1), str(file_2)]}
    size = sum(os.path.getsize(file) for file in dict_files["all_files"])
    percent_file_2 = int(os.path.getsize(str(file_2)) / size * 100)

    show_disk_usage(dict_files)

    captured = capsys.readouterr().out.split("\n")[0]
    assert captured == (
        f"'{_get_printable_file_path(str(file_2))}':        "
        + f"{os.path.getsize(file_2)} ({percent_file_2}%)"
      )