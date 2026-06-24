import csv
import json
from pathlib import Path

from pydantic import ValidationError

from models.match_model import MatchDto

BASE_DIR = Path(__file__).resolve().parent
MATCHES_DIR = BASE_DIR.parent / "data" / "matches_raw"

OUTPUT_DIR = BASE_DIR.parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "champions_versus.csv"
ERRORS_DIR = BASE_DIR.parent / "data" / "champions_versus_errors"


def is_error_response(raw: dict) -> bool:
    """Detecta si el JSON es una respuesta de error de la API en vez de un partido."""
    return "status" in raw and "info" not in raw


def extract_match_summary(match: MatchDto) -> dict:
    info = match.info
    team_100 = sorted(p.championName for p in info.participants if p.teamId == 100)
    team_200 = sorted(p.championName for p in info.participants if p.teamId == 200)
    winner = next((t.teamId for t in info.teams if t.win), None)
    return {
        "match_id": match.metadata.matchId,
        "game_version": info.gameVersion,
        "game_duration_sec": info.gameDuration,
        "queue_id": info.queueId,
        "team_100_champions": "|".join(team_100),
        "team_200_champions": "|".join(team_200),
        "winning_team": winner,
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ERRORS_DIR.mkdir(parents=True, exist_ok=True)

    json_files = sorted(MATCHES_DIR.glob("*.json"))
    if not json_files:
        print(f"No se encontraron ficheros JSON en {MATCHES_DIR}")
        return

    rows = []
    stats = {"ok": 0, "api_error": 0, "validation_error": 0, "other": 0}

    for json_file in json_files:
        try:
            raw_text = json_file.read_text(encoding="utf-8")
            raw_dict = json.loads(raw_text)

            # Filtro 1: respuestas de error de la API
            if is_error_response(raw_dict):
                stats["api_error"] += 1
                continue

            # Filtro 2: validar contra el modelo
            match = MatchDto.model_validate(raw_dict)
            rows.append(extract_match_summary(match))
            stats["ok"] += 1

        except ValidationError as e:
            stats["validation_error"] += 1
            # Guardamos el error para analizarlo después
            (ERRORS_DIR / f"{json_file.stem}.txt").write_text(str(e), encoding="utf-8")
        except Exception as e:
            stats["other"] += 1
            print(f"Error inesperado en {json_file.name}: {e}")

    # Escribir CSV
    if rows:
        with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

    # Reporte
    print(f"\n--- Resumen ---")
    print(f"  OK:                 {stats['ok']}")
    print(f"  Errores API (429):  {stats['api_error']}")
    print(f"  Errores validación: {stats['validation_error']}")
    print(f"  Otros errores:      {stats['other']}")
    print(f"\nCSV → {OUTPUT_FILE}")
    if stats["validation_error"]:
        print(f"Detalles de errores de validación → {ERRORS_DIR}")


if __name__ == "__main__":
    main()