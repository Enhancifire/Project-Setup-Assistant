from .generator import create_django_app
import subprocess


def dmain():
    a = subprocess.run("ls")
    print(a)
