from modules.django import django
from modules.flask import flask
from modules.git import git
import os
from modules.main import main as main_module
from pyfzf.pyfzf import FzfPrompt


def runfzf(tech):
    """Runs FZF Selection Prompt
    Takes a list or dictionary of items and returns single string"""
    fzf = FzfPrompt()
    choice = fzf.prompt(tech)
    return choice[0]


def choose():
    """Choose the Framework to be setup"""
    tech = {
        "Django": django.dmain,
        "Flask": flask.create,
    }

    choice = runfzf(tech)

    a = tech[choice]
    a()


def main():
    """
    Main Function running the project
    Uses FZF for user choice selection and runs appropriate function
    """
    CONFIG = main_module.load()

    path = CONFIG["PROJECT"]["PROJECT_DIR"]

    choose()

    print(path)

    os.chdir(path)
    print(os.getcwd())


if __name__ == "__main__":
    main()
