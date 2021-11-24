import sys
import os

_CURRENT_DIRECTORY: str = os.path.abspath(os.path.dirname(__file__))
_ROOT_DIRECTORY: str = os.path.join(_CURRENT_DIRECTORY, "..")

sys.path.append(_ROOT_DIRECTORY)
