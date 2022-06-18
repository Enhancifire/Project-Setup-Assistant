import subprocess
import os


def generate():
    create_python_script()
    make_templates()
    pass


def create_python_script():
    contents = f"""
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
"""

    with open("app.py", "w") as f:
        f.write(contents)


def make_templates():
    subprocess.run(["mkdir", "templates"])
    subprocess.run(["touch", os.path.join("templates", "base.html")])
    subprocess.run(["touch", os.path.join("templates", "index.html")])
