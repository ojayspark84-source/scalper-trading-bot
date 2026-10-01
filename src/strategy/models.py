from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Signal(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass(frozen=True)
class Candle:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0


@dataclass(frozen=True)
class TradeSignal:
    signal: Signal
    confidence: float
    price: float
    reason: str
    timestamp: datetime
