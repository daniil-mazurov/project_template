import os
import sys

import pdoc
from pdoc.render import configure

# Добавляем путь к директории проекта в системный путь
sys.path.insert(1, os.path.dirname(sys.path[0]))

from core.path import PATH

PROG_NAME = ""
BRANCH = "master"


def create_docs():
    """Создает документацию для проекта с использованием pdoc.

    Эта функция настраивает параметры генерации документации и вызывает
    pdoc для создания документации из исходного кода проекта.

    Настройки документации включают формат документации, логотип, ссылку на логотип
    и URL для редактирования исходного кода на GitHub.

    Returns:
        None
    """
    configure(
        docformat="google",
        edit_url_map={
            "src": f"https://github.com/daniil-mazurov/{PROG_NAME}/blob/{BRANCH}/src/"
        },
    )
    pdoc.pdoc(PATH / "src", output_directory=PATH / "docs")


if __name__ == "__main__":
    create_docs()
