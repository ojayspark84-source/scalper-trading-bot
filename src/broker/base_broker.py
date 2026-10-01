from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from src.strategy.models import Signal


@dataclass(frozen=True)
class OrderResult:
    accepted: bool
    signal: Signal
    stake: float
    price: float
    timestamp: datetime
    message: str = ""


class Broker(ABC):
    @abstractmethod
    def place_order(self, signal: Signal, stake: float, price: float) -> OrderResult:
        pass

    @abstractmethod
    def balance(self) -> float:
        pass
