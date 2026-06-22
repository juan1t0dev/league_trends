from pathlib import Path
from types import SimpleNamespace
import yaml


def _to_namespace(value):
    if isinstance(value, dict):
        return SimpleNamespace(**{k: _to_namespace(v) for k, v in value.items()})
    return value


def _replace_in_namespace(ns, replacements):
    for key, value in vars(ns).items():
        if isinstance(value, str):
            for placeholder, replacement in replacements.items():
                value = value.replace(f"{{{placeholder}}}", replacement)
            setattr(ns, key, value)
        elif isinstance(value, SimpleNamespace):
            _replace_in_namespace(value, replacements)


class _Config:
    assets: SimpleNamespace
    constants: SimpleNamespace
    data: SimpleNamespace

    def __init__(self, data: dict) -> None:
        for k, v in data.items():
            setattr(self, k, _to_namespace(v))

    def __repr__(self) -> str:
        return f"Config({vars(self)!r})"

    def set_latest_versions(self):
        from data_dragon.versions import Versions
        replacements = {
            "version": Versions.get_latest_version(),
            "minimaps_version": Versions.minimaps_version,
            "scoreboard_icons_version": Versions.scoreboard_icons_version,
        }
        _replace_in_namespace(self, replacements)

    def set_language(self,language):
        replacements = {"language" : language}
        _replace_in_namespace(self, replacements)


_config_path = Path(__file__).parent.parent.parent / "config.yml"

with open(_config_path) as f:
    Config = _Config(yaml.safe_load(f))
