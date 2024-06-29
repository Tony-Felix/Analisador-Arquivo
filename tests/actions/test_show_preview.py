import pytest
from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.mark.parametrize(
    "context, output",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']\n""",
        ),
        (
            {
                "all_files": [],
                "all_dirs": [],
            },
            "Found 0 files and 0 directories\n",
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                    "src/app/__init__.py",
                    "src/utils/__finesh__.py",
                    "src/models/__init__.py",
                    "src/services/__init__.py",
                ],
                "all_dirs": [
                    "src",
                    "src/utils",
                    "src/models",
                    "src/services",
                    "src/tests",
                    "src/database",
                    "src/config",
                ],
            },
            (
                "Found 7 files and 7 directories\n"
                "First 5 files: ['src/__init__.py', "
                "'src/app.py', 'src/utils/__init__.py', "
                "'src/app/__init__.py', "
                "'src/utils/__finesh__.py']\n"
                "First 5 directories: ['src', 'src/utils', 'src/models', "
                "'src/services', 'src/tests']\n"
            ),
        ),
    ],
)
def test_show_preview(capsys, context, output):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == output
