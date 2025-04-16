import os
import urllib.request

PRETTY_TOOL_DIR = os.path.join(os.getenv("HOME"), ".pretty_tool")
PRETTY_PHP_PATH = os.path.join(PRETTY_TOOL_DIR, "pretty-php.phar")
PRETTY_PHP_URL = (
    "https://github.com/lkrms/pretty-php/releases/latest/download/pretty-php.phar"
)

if not os.path.exists(PRETTY_TOOL_DIR):
    os.mkdir(PRETTY_TOOL_DIR)

if not os.path.exists(PRETTY_PHP_PATH):
    urllib.request.urlretrieve(
        PRETTY_PHP_URL, os.path.join(PRETTY_TOOL_DIR, "pretty-php.phar")
    )
