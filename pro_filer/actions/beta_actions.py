"""Arquivo que estudantes devem editar"""

import os


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=lambda x: x.count("/"))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    return [
        path
        for path in context["all_files"]
        if (case_sensitive and search_term in os.path.basename(path))
        or (
            not case_sensitive
            and search_term.lower() in os.path.basename(path).lower()
        )
    ]
