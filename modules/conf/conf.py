import subprocess
import os
from pytermgui import tim


def lang_spec(lang, projname, CONF):
    """Performs Language Specific Setup"""

    if lang == "Python":
        virt_python(projname, CONF)


def virt_python(projname, CONF):
    """Creates virtual environment for python"""

    current_path = os.getcwd()

    virt_path = CONF["PROJECT"]["PYTHON_VIRTUALENV_DIR"]

    os.chdir(virt_path)
    subprocess.run(["virtualenv", f"{projname}"])
    os.chdir(current_path)

    tim.print(
        f"[green bold]Virtualenv Created at {os.path.join(virt_path, projname)}[/green /bold]"
    )
    tim.print(
        f"To activate, type [italic blue]source {os.path.join(virt_path, projname, 'bin')}[/italic]"
    )
