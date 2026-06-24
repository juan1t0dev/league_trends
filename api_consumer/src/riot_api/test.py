import os
import json
import time
from collections import deque
from pathlib import Path
import requests
from dotenv import load_dotenv


class RiotRateLimiter:
    """Riot API Limits: 20 req/1s y 100 req/2min."""

    def __init__(self):
        self.short_window = deque()
        self.long_window = deque()
        self.SHORT_LIMIT = 20
        self.SHORT_WINDOW = 1.0
        self.LONG_LIMIT = 100
        self.LONG_WINDOW = 120.0

    def _clean(self, now: float) -> None:
        """Remove timestamp outsife of window."""
        while self.short_window and now - self.short_window[0] > self.SHORT_WINDOW:
            self.short_window.popleft()
        while self.long_window and now - self.long_window[0] > self.LONG_WINDOW:
            self.long_window.popleft()

    def wait_if_needed(self) -> None:
        """Wait if any window is full."""
        while True:
            now = time.monotonic()
            self._clean(now)

            if len(self.short_window) >= self.SHORT_LIMIT:
                # Hay que esperar hasta que salga el más antiguo de la ventana corta
                sleep_for = self.SHORT_WINDOW - (now - self.short_window[0]) + 0.01
                print(f" Short limit reached. Waiting {sleep_for:.2f}s...")
                time.sleep(sleep_for)
                continue

            if len(self.long_window) >= self.LONG_LIMIT:
                sleep_for = self.LONG_WINDOW - (now - self.long_window[0]) + 0.01
                print(f" Long limit reached. Waiting {sleep_for:.1f}s...")
                time.sleep(sleep_for)
                continue

            # Hay hueco: registramos esta petición
            self.short_window.append(now)
            self.long_window.append(now)
            return


def safe_get(url: str, params: dict, limiter: RiotRateLimiter, max_retries: int = 3):
    """GET with rate limiter + retries if 429."""
    for attempt in range(max_retries):
        limiter.wait_if_needed()
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            # Backup: si por algún motivo la API igualmente nos limita
            wait = int(response.headers.get("Retry-After", 10))
            print(f" 429 received. Waiting {wait}s (try {attempt + 1}/{max_retries})")
            time.sleep(wait)
            continue

        print(f" Error {response.status_code}: {response.text[:120]}")
        return None

    return None


def main():
    load_dotenv()
    api_key = os.environ['RIOT_API_KEY']
    limiter = RiotRateLimiter()

    # 1. Get players from division
    division_uri = 'https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/I'
    entries = safe_get(division_uri, {'page': 1, 'api_key': api_key}, limiter)

    if not isinstance(entries, list):
        print(f"Unexpected answer: {entries}")
        return

    puuids = {e['puuid'] for e in entries}
    print(f'Players: {len(puuids)}')

    # 2. Get last 20 matches from each player
    matches_uri = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'
    seen_matches = set()

    for i, puuid in enumerate(puuids, 1):
        print(f"[{i}/{len(puuids)}] Matches from {puuid[:12]}...")
        url = matches_uri.replace('{puuid}', puuid)
        params = {
            'queue': 420, 'type': 'ranked', 'start': 0, 'count': 20,
            'api_key': api_key,
        }
        player_matches = safe_get(url, params, limiter)
        if isinstance(player_matches, list):
            seen_matches.update(player_matches)

    print(f'Unique matches: {len(seen_matches)}')

    # 3. Get deatiled match JSON
    data_dir = Path(__file__).resolve().parent / 'data' / 'matches'
    data_dir.mkdir(parents=True, exist_ok=True)
    detail_uri = 'https://europe.api.riotgames.com/lol/match/v5/matches/{matchid}'

    saved = 0
    skipped = 0
    for i, match_id in enumerate(seen_matches, 1):
        match_file = data_dir / f'{match_id}.json'

        # Idempotencia: no redescargar
        if match_file.exists() and match_file.stat().st_size > 1000:
            skipped += 1
            continue

        print(f"[{i}/{len(seen_matches)}] {match_id}")
        url = detail_uri.replace('{matchid}', match_id)
        match_data = safe_get(url, {'api_key': api_key}, limiter)

        if match_data is None:
            continue

        with open(match_file, 'w', encoding='utf-8') as f:
            json.dump(match_data, f, ensure_ascii=False, indent=2)
        saved += 1

    print(f'\n Saved {saved} new matches, {skipped} alredy existed at {data_dir}')


if __name__ == "__main__":
    main()