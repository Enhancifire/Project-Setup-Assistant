# import modules.django.main as django
# import modules.flask as flask
from pyfzf.pyfzf import FzfPrompt
import os
from modules.main.main import load


def runfzf(tech):
    fzf = FzfPrompt()
    choice = fzf.prompt(tech)
    return choice


def main():
    """
    Main Function running the project
    Uses FZF for user choice selection and runs appropriate function
    """
    CONFIG = load()

    # tech = {
    #     "Django": django.dmain,
    #     # "Flask": flask_test,
    # }

    # choice = runfzf(tech)

    # a = tech[choice[0]]
    # a()
    path = CONFIG["PROJECT"]["PROJECT_DIR"]

    print(path)

    os.chdir(path)
    print(os.getcwd())


if __name__ == "__main__":
    main()
