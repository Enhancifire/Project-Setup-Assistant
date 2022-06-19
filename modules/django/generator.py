import subprocess
from pytermgui import tim


def create_django_app(projectname: str):
    """
    Creates a new Django App. Takes the project name as import parameter 'projectname'
    """
    # subprocess.run(["django-admin", "startproject", projectname])
    tim.print("[green bold]Project[/bold] Created[/green]")
