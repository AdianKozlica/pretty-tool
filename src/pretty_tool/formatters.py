import subprocess
import jsbeautifier
import cssbeautifier
from bs4 import BeautifulSoup
import json


def py(code: str):
    return subprocess.check_output(
        ["python3", "-m", "ruff", "format", "-"], input=code.encode()
    ).decode()


def js(code: str):
    return jsbeautifier.beautify(code)


def jsx(code: str):
    return jsbeautifier.beautify(
        code,
        jsbeautifier.BeautifierOptions({"e4x": True, "space_before_conditional": True}),
    )


def css(code: str):
    return cssbeautifier.beautify(code)


def xml(code: str, parser="xml"):
    bs = BeautifulSoup(code, parser)
    return bs.prettify()


def html(code: str):
    return xml(code, "lxml")


def json_f(code: str):
    return json.dumps(json.loads(code), indent=2)
