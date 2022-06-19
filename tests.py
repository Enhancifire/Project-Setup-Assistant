from modules.django import django
from modules.flask import flask
from modules.git import git
from modules.main import config
from modules.main import main as main_module
from pytermgui import tim
import os

CONFIG = config.load()


def git_test():
    path = CONFIG["PROJECT"]["PROJECT_DIR"]

    os.chdir(os.path.join(path, "Testing", "Project Setup Tool Testing", "GitTesting"))
    git.git("Test")


def flask_testing():
    path = CONFIG["PROJECT"]["PROJECT_DIR"]
    os.chdir(
        os.path.join(path, "Testing", "Project Setup Tool Testing", "FlaskTesting")
    )

    flask.create()


def django_test():
    path = CONFIG["PROJECT"]["PROJECT_DIR"]
    os.chdir(
        os.path.join(path, "Testing", "Project Setup Tool Testing", "DjangoTesting")
    )

    django.dmain()


def virt_test():
    main_module.virt_python("ABC")


def main():
    tim.print("[!rainbow]Project Setup Tool Tests[/rainbow]")
    # tim.print("[green]Git Testing[/green]")
    # git_test()

    # tim.print("[blue]Flask Testing[/blue]")
    # flask_testing()

    # tim.print("[blue]Django Testing[/blue]")
    # django_test()

    virt_test()


if __name__ == "__main__":
    main()
