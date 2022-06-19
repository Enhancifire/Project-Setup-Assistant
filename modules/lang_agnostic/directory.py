import os
from pytermgui import tim


def create_dir(proj_name, path):
    proj_path = os.path.join(path, proj_name)
    try:
        os.mkdir(proj_path)
        return True
    except FileExistsError:
        tim.print("[red]Project already exists. Select different project name")
        return False
