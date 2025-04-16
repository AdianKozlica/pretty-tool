import subprocess
from bs4 import BeautifulSoup
from pathlib import Path

import os
import json
import shutil

NPX_EXISTS = shutil.which("npx") is not None
PHP_EXISTS = shutil.which("php") is not None
PRETTY_PHP_PATH = os.path.join(os.getenv("HOME"), ".pretty_tool/pretty-php.phar")
BIOME_CONFIG = str(Path(__file__).parent)


def clang_format(code: str, suffix: str):
    return subprocess.check_output(
        ["clang-format", f"--assume-filename=sample.{suffix}"], input=code.encode()
    ).decode()


def biome_format(code: str, suffix: str):
    if not NPX_EXISTS:
        raise OSError("NPX is not installed")

    return subprocess.check_output(
        [
            "npx",
            "@biomejs/biome",
            "format",
            f"--stdin-file-path=sample.{suffix}",
            f"--config-path={BIOME_CONFIG}",
        ],
        input=code.encode(),
    ).decode()


def py(code: str):
    return subprocess.check_output(
        ["python3", "-m", "ruff", "format", "-"], input=code.encode()
    ).decode()


def php(code: str):
    if not PHP_EXISTS:
        raise OSError("PHP is not installed!")

    return subprocess.check_output(
        ["php", PRETTY_PHP_PATH, "--stdin-filename=sample.php", "-qq"],
        input=code.encode(),
    ).decode()


def js(code: str):
    return biome_format(code, "js")


def ts(code: str):
    return biome_format(code, "ts")


def c(code: str):
    return clang_format(code, "c")


def cpp(code: str):
    return clang_format(code, "cpp")


def cs(code: str):
    return clang_format(code, "cs")


def m(code: str):
    return clang_format(code, "m")


def java(code: str):
    return clang_format(code, "java")


def jsx(code: str):
    return biome_format(code, "jsx")


def tsx(code: str):
    return biome_format(code, "tsx")


def css(code: str):
    return biome_format(code, "css")


def xml(code: str, parser="xml"):
    bs = BeautifulSoup(code, parser)
    return bs.prettify()


def html(code: str):
    return xml(code, "lxml")


def json_f(code: str):
    return json.dumps(json.loads(code), indent=2)
