from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Config:
    raw: dict[str, Any]

    def get(self, *keys: str, default: Any = None) -> Any:
        value: Any = self.raw
        for key in keys:
            if not isinstance(value, dict) or key not in value:
                return default
            value = value[key]
        return value


def load_config(path: str | Path) -> Config:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError("Configuration root must be a mapping")
    return Config(data)
