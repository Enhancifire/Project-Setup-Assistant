import subprocess


def create_django_app(projectname: str):
    """
    Creates a new Django App. Takes the project name as import parameter 'projectname'
    """
    subprocess.run(["django-admin", "starproject", projectname])
    return True
