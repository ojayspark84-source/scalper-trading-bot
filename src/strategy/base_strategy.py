from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence

from .models import Candle, TradeSignal


class BaseStrategy(ABC):
    @abstractmethod
    def generate_signal(self, candles: Sequence[Candle]) -> TradeSignal:
        """Return a signal from the supplied candles without placing a trade."""
