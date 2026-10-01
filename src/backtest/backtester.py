from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence

from src.strategy.base_strategy import BaseStrategy
from src.strategy.models import Candle, Signal


@dataclass
class BacktestResult:
    starting_balance: float
    ending_balance: float
    trades: int
    wins: int
    losses: int

    @property
    def win_rate(self) -> float:
        return self.wins / self.trades if self.trades else 0.0


class Backtester:
    def __init__(self, strategy: BaseStrategy, stake: float, payout: float = 0.8,
                 starting_balance: float = 1000.0) -> None:
        self.strategy, self.stake, self.payout = strategy, stake, payout
        self.starting_balance = starting_balance

    def run(self, candles: Sequence[Candle]) -> BacktestResult:
        balance, trades, wins, losses = self.starting_balance, 0, 0, 0
        for index in range(1, len(candles)):
            signal = self.strategy.generate_signal(candles[:index])
            if signal.signal == Signal.HOLD:
                continue
            trades += 1
            won = (signal.signal == Signal.BUY and candles[index].close > candles[index - 1].close) or \
                  (signal.signal == Signal.SELL and candles[index].close < candles[index - 1].close)
            if won:
                balance += self.stake * self.payout
                wins += 1
            else:
                balance -= self.stake
                losses += 1
        return BacktestResult(self.starting_balance, balance, trades, wins, losses)
