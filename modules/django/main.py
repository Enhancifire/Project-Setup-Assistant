from .generator import generate
import subprocess

def dmain():
    a = subprocess.run("ls")
    print(a)
