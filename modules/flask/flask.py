import subprocess
import os
from .generator import generate


def create():
    generate()
    print("Flask App Created")
