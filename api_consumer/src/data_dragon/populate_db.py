from champions import Champions
from pathlib import Path

CHAMPIONS_DB = Path(__file__).resolve().parent / "champions_db"

def main():
    champions_db_dir = Path(__file__).resolve().parent / 'champions_db'
    champions_db_dir.mkdir(parents=True, exist_ok=True)

# TBD: Fetch champions and store them

if __name__ == "__main__":
    main()