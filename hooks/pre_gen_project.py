"""This module is called before project is created."""

import re
import sys

MODULE_NAME = "{{ cookiecutter.module_name }}"
MODULE_VERSION = "{{ cookiecutter.version }}"


MODULE_REGEX = re.compile(r"^[a-z][a-z0-9\-\_]+[a-z0-9]$")
SEMVER_REGEX = re.compile(
    r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """,
    re.VERBOSE,
)


def validate_module_name(module_name: str) -> None:
    """Ensure that `module_name` parameter is valid.
    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.
    Args:
        module_name: current module name
    Raises:
        ValueError: If module_name is not a valid Python module name
    """
    if MODULE_REGEX.fullmatch(module_name) is None:
        message = f"ERROR: The module name `{module_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_semver(version: str) -> None:
    """Ensure version in semver notation.
    Args:
        version: string version. For example 0.1.2 or 1.2.4
    Raises:
        ValueError: If version is not in semver notation
    """
    if SEMVER_REGEX.fullmatch(version) is None:
        message = f"ERROR: The `{version}` is not in semver notation (https://semver.org/)"
        raise ValueError(message)


def main() -> None:
    try:
        validate_module_name(module_name=MODULE_NAME)
        validate_semver(version=MODULE_VERSION)
    except ValueError as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()