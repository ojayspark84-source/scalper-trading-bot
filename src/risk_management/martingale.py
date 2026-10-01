from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Martingale:
    base_amount: float
    multiplier: float = 1.05
    max_steps: int = 3
    step: int = 0

    def next_stake(self) -> float:
        return round(self.base_amount * (self.multiplier ** self.step), 2)

    def record_win(self) -> None:
        self.step = 0

    def record_loss(self) -> None:
        self.step = min(self.step + 1, self.max_steps)

    def reset(self) -> None:
        self.step = 0
