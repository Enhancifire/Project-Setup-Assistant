import subprocess
import os


def git(project_name):
    """Creates Git Repository and README and makes initial commit"""
    init(project_name)
    commit()


def safe():
    """Sets git repo as safe in git"""
    cwd = os.getcwd()
    subprocess.run(["git", "config", "--global", "--add", "safe.directory", cwd])


def init(pname):
    """
    Initializes a git repo and adds all files
    """
    subprocess.run(["git", "init", "."])
    create_readme(pname)
    safe()
    subprocess.run(["git", "branch", "-M", "main"])


def create_readme(pname):
    """Creates a README file"""

    with open("README.md", "w") as f:
        title = f"""# {pname} Project

## Dependancies

## Deployment

Created by:
"""
        f.write(title)


def commit():
    """Makes the Initial Commit"""
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", "'Initial Commit'"])
