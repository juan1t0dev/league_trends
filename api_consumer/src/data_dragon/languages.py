import requests
from .config import Config

class Languages:

    @staticmethod
    def get_languages():
        return requests.get(Config.constants.languages).json()