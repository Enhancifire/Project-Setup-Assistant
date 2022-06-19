import subprocess
import os
from .generator import generate


def create():
    """Generates Flask Boilerplate"""
    generate()
    print("Flask App Created")


def test():

    """Function used to test import of Flask module during development"""
    print("Flask Module Called")
