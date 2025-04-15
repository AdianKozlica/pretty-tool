import subprocess
import jsbeautifier
import cssbeautifier
from bs4 import BeautifulSoup


def py(code: str):
    return subprocess.check_output(
        ["python3", "-m", "ruff", "format", "-"], input=code.encode()
    ).decode()


def js(code: str):
    return jsbeautifier.beautify(code)


def css(code: str):
    return cssbeautifier.beautify(code)


def xml(code: str, parser="xml"):
    bs = BeautifulSoup(code, parser)
    return bs.prettify()


def html(code: str):
    return xml(code, "lxml")
