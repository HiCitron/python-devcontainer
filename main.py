import pydicom

import os

API_KEY = os.environ.get("API_KEY")
if API_KEY is None:
    raise Exception("API key not set")

print(pydicom.__version__)


def add(x: int, y: int) -> int:
    return x+y