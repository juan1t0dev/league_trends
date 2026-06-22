import requests
from .config import Config

class Champions:

    @staticmethod
    def get_all_champions():
        return requests.get(Config.data.champions).json()["data"]

    @staticmethod
    def get_champion_byName(champion_name):
        return requests.get(Config.data.champions).json()["data"][champion_name]
    
    @staticmethod
    def get_all_champions_ranged():
        champions_raw = requests.get(Config.data.champions).json()["data"]
        return [name for name, data in champions_raw.items() if data["stats"]["attackrange"] > 350]
    
    @staticmethod
    def get_all_champions_melee():
        champions_raw = requests.get(Config.data.champions).json()["data"]
        return [name for name, data in champions_raw.items() if data["stats"]["attackrange"] <= 350]