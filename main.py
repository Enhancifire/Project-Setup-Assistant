from modules.django import django
from modules.flask import flask
from modules.git import git
from modules.conf import conf
from modules.conf import config
from pyfzf.pyfzf import FzfPrompt
from modules.lang_agnostic import directory
from pytermgui import tim
import os


def runfzf(tech):
    """Runs FZF Selection Prompt
    Takes a list or dictionary of items and returns single string"""
    fzf = FzfPrompt()
    choice = fzf.prompt(tech)
    return choice[0]


def choose():
    """Choose the Framework to be setup"""
    tech = {
        "Python": {
            "Django": django.dmain,
            "Flask": flask.create,
        },
    }

    lang = runfzf(tech)
    choice = runfzf(tech[lang])
    func = tech[lang][choice]

    return func, lang, choice


def main():
    """
    Main Function running the project
    Uses FZF for user choice selection and runs appropriate function
    """
    # Load configuration
    CONFIG = config.load()
    path = CONFIG["PROJECT"]["PROJECT_DIR"]

    # Take input of project name
    projname = input("Enter project name: ")

    # Create directory
    if directory.create_dir(projname, path):

        # Change to project direcory after creation
        os.chdir(os.path.join(path, projname))

        # Choose language and framework
        func, lang, _ = choose()

        # Language Specific Setup
        conf.lang_spec(lang, projname, CONFIG)

        # Setup Project
        func()

        # Setup Git Repository
        git.git(projname)

        tim.print(f"[bold yellow]Project '{projname}' created successfully")

    else:
        return


if __name__ == "__main__":
    main()
