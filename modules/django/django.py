from .generator import create_django_app
import subprocess
from pytermgui import tim


def dmain():
    """Creates the main Django app"""
    projectname = input("Enter Django Project/App name: ")
    create_django_app(projectname)


def test():
    """Function used to test import of django module during development"""
    tim.print("[red bold]Django Module Called[/red /bold]")
