#!/usr/bin/python3
import sys
import argparse
from pretty_tool.formatters import *

LANGUAGES = {
    "py": py,
    "php": php,
    "js": js,
    "ts": ts,
    "c": c,
    "cpp": cpp,
    "cs": cs,
    "m": m,  # Objective-C
    "java": java,
    "jsx": jsx,
    "tsx": tsx,
    "css": css,
    "xml": xml,
    "html": html,
    "json": json_f,
}


def main():
    parser = argparse.ArgumentParser(
        prog="pretty_tool", description="Universal prettifier."
    )
    parser.add_argument("language", help="Language code", default=None, nargs="?")
    parser.add_argument(
        "input_file", help="Path to the input file", default=None, nargs="?"
    )
    parser.add_argument(
        "-l", "--languages", help="Show all language codes", action="store_true"
    )
    args = parser.parse_args()

    if args.languages:
        print("Available language codes: ", ", ".join(LANGUAGES))
        exit(0)

    if args.language is None:
        raise argparse.ArgumentError(
            args.language, message="You need to select a language code!"
        )

    if args.input_file is None:
        raise argparse.ArgumentError(
            args.input_file, message="You need to select an input file!"
        )

    if args.language not in LANGUAGES:
        print("Language not supported!", file=sys.stderr)
        exit(1)

    with open(args.input_file, "r") as file:
        formatter = LANGUAGES[args.language]
        print(formatter(file.read()))
