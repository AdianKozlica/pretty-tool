#!/usr/bin/python3
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal prettifier.")
    parser.add_argument("language", help="Language code")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument(
        "-l", "--languages", help="Show all language codes", action="store_true"
    )
    args = parser.parse_args()
