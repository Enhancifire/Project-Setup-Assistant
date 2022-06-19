from modules.django import django
from modules.flask import flask
from modules.git import git
from modules.conf import conf
from modules.conf import config
from modules.lang_agnostic import directory
from pytermgui import tim
import os
import inquirer


def select(tech):
    """Tech Selection Prompt"""

    lang_list = [
        inquirer.List(
            "lang", message="Select a Language", choices=[lang for lang in tech]
        )
    ]

    lang = inquirer.prompt(lang_list)["lang"]

    framework_list = [
        inquirer.List(
            "framework",
            message="Select Framwork",
            choices=[frame for frame in tech[lang]],
        )
    ]

    framework = inquirer.prompt(framework_list)["framework"]

    return tech[lang][framework], lang, framework


def main():
    """
    Main Function running the project
    Uses FZF for user choice selection and runs appropriate function
    """
    # Load configuration
    CONFIG = config.load()
    path = CONFIG["PROJECT"]["PROJECT_DIR"]
    is_fzf = CONFIG["FZF"]

    tech = {
        "Python": {
            "Django": django.dmain,
            "Flask": flask.create,
        },
    }

    try:
        # Take input of project name
        projname = input("Enter project name: ")

        # Create directory
        if directory.create_dir(projname, path):

            # Change to project direcory after creation
            os.chdir(os.path.join(path, projname))

            # Choose language and framework
            if is_fzf:
                from modules.fzf import fzf

                func, lang, _ = fzf.choose(tech)

            else:
                func, lang, _ = select(tech)

            # Language Specific Setup
            conf.lang_spec(lang, projname, CONFIG)

            # Setup Project
            func()

            # Setup Git Repository
            git.git(projname)

            tim.print(f"[bold yellow]Project '{projname}' created successfully")

        else:
            return

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
