import os
import sys

from bentoml import archive
from bentoml.cli import create_bentoml_cli

__VERSION__ = "2019_06_26_2ca97a3f"

__module_path = os.path.abspath(os.path.dirname(__file__))

PassengerClassifier = archive.load_bento_service_class(__module_path)

cli=create_bentoml_cli(__module_path)


def load():
    return archive.load(__module_path)


__all__ = ['__version__', 'PassengerClassifier', 'load']
