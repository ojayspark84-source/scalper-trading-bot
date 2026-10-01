from __future__ import annotations

from datetime import datetime, timezone

from .base_broker import Broker, OrderResult
from src.strategy.models import Signal


class PaperBroker(Broker):
    """Safe broker adapter: records simulated orders and never contacts a live API."""

    def __init__(self, starting_balance: float = 1000.0) -> None:
        self._balance = starting_balance

    def place_order(self, signal: Signal, stake: float, price: float) -> OrderResult:
        return OrderResult(True, signal, stake, price, datetime.now(timezone.utc), "paper order")

    def balance(self) -> float:
        return self._balance
