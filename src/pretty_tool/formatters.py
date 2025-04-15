import subprocess
import jsbeautifier
import cssbeautifier


def py(code: str):
    print(
        subprocess.check_output(
            ["python3", "-m", "ruff", "format", "-"], input=code.encode()
        ).decode()
    )


def js(code: str):
    print(jsbeautifier.beautify(code))


def css(code: str):
    print(cssbeautifier.beautify(code))
