# Inspired by [python-package-template](https://github.com/TezRomacH/python-package-template)
"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
MODULE_DIRECTORY = Path.cwd().absolute()
MODULE_NAME = "{{ cookiecutter.module_name }}"
MODULE_MODULE = "{{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_') }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_name }}"

licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Lesser GNU GPL v3.0": "lgpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license(directory: Path, licence: str) -> None:
    """Generate license file for the project.
    Args:
        directory: path to the project directory
        licence: chosen licence
    """
    move(str(directory / "_licenses" / f"{licence}.txt"), str(directory / "LICENSE"))
    rmtree(str(directory / "_licenses"))


def print_futher_instuctions(module_name: str, github: str) -> None:
    """Show user what to do next after project creation.
    Args:
        module_name: current project name
        github: GitHub username
    """
    message = f"""
    Your module {module_name} is created.
    1) Now you can start working on it:
        $ cd {module_name} && git init
    2) If you don't have pip install it
    3) Run the make command to use pip to build the wheel package or install in your environment
        $ make wheel
        $ make install
    4) Upload initial code to GitHub:
        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{module_name}.git
        $ git push -u origin main
    """
    print(textwrap.dedent(message))


def main() -> None:
    generate_license(directory=MODULE_DIRECTORY, licence=licences_dict[LICENSE])
    print_futher_instuctions(module_name=MODULE_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()