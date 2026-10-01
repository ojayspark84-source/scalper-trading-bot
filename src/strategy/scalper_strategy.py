from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime, timezone

from .base_strategy import BaseStrategy
from .models import Candle, Signal, TradeSignal


def ema(values: Sequence[float], period: int) -> float:
    if not values:
        raise ValueError("At least one value is required")
    alpha = 2 / (period + 1)
    result = values[0]
    for value in values[1:]:
        result = alpha * value + (1 - alpha) * result
    return result


def rsi(values: Sequence[float], period: int) -> float:
    if len(values) <= period:
        return 50.0
    gains, losses = [], []
    for previous, current in zip(values[-period - 1:-1], values[-period:]):
        change = current - previous
        gains.append(max(change, 0))
        losses.append(max(-change, 0))
    average_loss = sum(losses) / period
    if average_loss == 0:
        return 100.0
    return 100 - (100 / (1 + (sum(gains) / period) / average_loss))


class ScalperStrategy(BaseStrategy):
    def __init__(self, fast_ema: int = 5, slow_ema: int = 13, rsi_period: int = 7,
                 rsi_oversold: float = 30, rsi_overbought: float = 70,
                 minimum_confidence: float = 0.60) -> None:
        self.fast_ema = fast_ema
        self.slow_ema = slow_ema
        self.rsi_period = rsi_period
        self.rsi_oversold = rsi_oversold
        self.rsi_overbought = rsi_overbought
        self.minimum_confidence = minimum_confidence

    def generate_signal(self, candles: Sequence[Candle]) -> TradeSignal:
        if len(candles) < max(self.slow_ema, self.rsi_period + 1):
            return TradeSignal(Signal.HOLD, 0.0, candles[-1].close if candles else 0.0,
                               "insufficient candle history", datetime.now(timezone.utc))
        closes = [c.close for c in candles]
        fast, slow = ema(closes, self.fast_ema), ema(closes, self.slow_ema)
        current_rsi = rsi(closes, self.rsi_period)
        confidence = min(1.0, abs(fast - slow) / max(slow * 0.001, 1e-12) / 10)
        if fast > slow and current_rsi < self.rsi_overbought:
            signal = Signal.BUY
            reason = f"EMA bullish crossover bias; RSI={current_rsi:.1f}"
        elif fast < slow and current_rsi > self.rsi_oversold:
            signal = Signal.SELL
            reason = f"EMA bearish crossover bias; RSI={current_rsi:.1f}"
        else:
            signal, reason = Signal.HOLD, f"no confirmed setup; RSI={current_rsi:.1f}"
        confidence = max(confidence, self.minimum_confidence if signal != Signal.HOLD else 0.0)
        return TradeSignal(signal, confidence, candles[-1].close, reason, candles[-1].timestamp)
