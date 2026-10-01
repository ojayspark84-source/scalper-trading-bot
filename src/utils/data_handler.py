from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from src.strategy.models import Candle


def load_csv(path: str | Path) -> list[Candle]:
    candles: list[Candle] = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            candles.append(Candle(datetime.fromisoformat(row["timestamp"]), float(row["open"]),
                                  float(row["high"]), float(row["low"]), float(row["close"]),
                                  float(row.get("volume", 0) or 0)))
    return candles
