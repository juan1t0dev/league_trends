import os
from dotenv import load_dotenv
from data_dragon.versions import Versions
from data_dragon.languages import Languages
from data_dragon.champions import Champions
from data_dragon.config import Config
from pprint import pprint

def main():
    load_dotenv()
    print(os.environ.get('RIOT_API_KEY'))
    Config.set_latest_versions()
    Config.set_language("en_US")
    pprint(vars(Config))
    print(Champions.get_champion_byName("Kayn"))
    print(len(Champions.get_all_champions_ranged()))
    print(len(Champions.get_all_champions_melee()))
if __name__ == "__main__":
    main()