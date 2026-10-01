from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from src.strategy.models import Signal


class TradeStatus(str, Enum):
    OPEN = "OPEN"
    WON = "WON"
    LOST = "LOST"


@dataclass
class Position:
    signal: Signal
    stake: float
    entry: float
    opened_at: datetime
    exit: float | None = None
    pnl: float = 0.0
    status: TradeStatus = TradeStatus.OPEN
