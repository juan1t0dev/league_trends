import os
import json
from pathlib import Path

import requests
from dotenv import load_dotenv



def main():
    load_dotenv()

    # Obtain players from a division
    division_uri = 'https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/I?page=1'

    api_param = {'api_key': os.environ['RIOT_API_KEY']}
    entries = requests.get(division_uri, params=api_param).json()
    puuids = {entry['puuid'] for entry in entries}
    print(puuids)
    print(f'Number of players: {len(puuids)}')

    # Obtain last 20 matches from each player (distinct)

    matches_uri = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'

    params = {
        'queue': 420,
        'type': 'ranked',
        'start': 0,
        'count': 20,
        'api_key': os.environ['RIOT_API_KEY'],
    }

    matches = []
    seen_matches = set()

    for p in puuids:
        player_matches_uri = matches_uri.replace('{puuid}', p)
        matches_per_player = requests.get(player_matches_uri, params=params).json()

        for match_id in matches_per_player:
            if match_id not in seen_matches:
                seen_matches.add(match_id)
                matches.append(match_id)

    print(matches)
    print(f'Total distinct matches: {len(matches)}')
    
    # Get detailed matches json from API and store them to perform analysis

    data_dir = Path(__file__).resolve().parent / 'data' / 'matches'
    data_dir.mkdir(parents=True, exist_ok=True)

    detailed_match_uri = 'https://europe.api.riotgames.com/lol/match/v5/matches/{matchid}'

    params = {'api_key': os.environ['RIOT_API_KEY']}

    detailed_matches = []

    for m in seen_matches:
        search_detail_uri = detailed_match_uri.replace('{matchid}', m)
        detailes_matches = requests.get(search_detail_uri, params=params).json()

        match_file = data_dir / f'{m}.json'
        with open(match_file, 'w', encoding='utf-8') as f:
            json.dump(detailes_matches, f, ensure_ascii=False, indent=2)

        detailed_matches.append(detailes_matches)

    print(f'Saved {len(detailed_matches)} detailed matches in {data_dir}')

if __name__ == "__main__":
    main()
