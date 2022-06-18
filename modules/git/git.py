import subprocess


def git(project_name):
    init_and_add(project_name)
    commit()


def init_and_add(pname):
    """
    Initializes a git repo and adds all files
    """
    subprocess.run(["git", "init", "."])
    create_readme(pname)
    subprocess.run(["git", "add", "-A"])


def create_readme(pname):
    """Creates a README file"""

    with open("README.md", "w") as f:
        title = f"""
        # {pname} Project

        Created by:
        Date Created:
        """
        f.write(title)


def commit():
    subprocess.run(["git", "commit", "-m", "'Initial Commit'"])
