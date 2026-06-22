import requests
from .config import Config

class Versions:

    # NOTE: this numbers are hardcoded because Riot doesn´t provide any official docommentation in regard
    # of this versions of the API, therefore they should be updated manuallu
    minimaps_version = "6.8.1"
    scoreboard_icons_version = "5.5.1"

    @staticmethod
    def get_versions():
        return requests.get(Config.constants.versions).json()
    
    @staticmethod
    def get_latest_version():
        return requests.get(Config.constants.versions).json()[0]