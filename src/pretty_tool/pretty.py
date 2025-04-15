#!/usr/bin/python3
import sys
import argparse
from pretty_tool.formatters import *

LANGUAGES = {
    "py": py,
    "js": js,
    "css": css,
    "xml": xml,
    "html": html,
}


def main():
    parser = argparse.ArgumentParser(
        prog="pretty_tool", description="Universal prettifier."
    )
    parser.add_argument("language", help="Language code")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument(
        "-l", "--languages", help="Show all language codes", action="store_true"
    )
    args = parser.parse_args()

    if args.language not in LANGUAGES:
        print("Language not supported!", file=sys.stderr)
        exit(1)

    with open(args.input_file, "r") as file:
        formatter = LANGUAGES[args.language]
        print(formatter(file.read()))
