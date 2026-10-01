from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskManager:
    starting_balance: float
    stop_loss: float
    max_daily_loss: float
    max_trade_risk_percent: float
    daily_pnl: float = 0.0

    def can_trade(self, balance: float, stake: float) -> tuple[bool, str]:
        if self.daily_pnl <= -abs(self.max_daily_loss):
            return False, "daily loss limit reached"
        if balance <= 0:
            return False, "account balance is not positive"
        if stake > balance * self.max_trade_risk_percent / 100:
            return False, "stake exceeds configured risk percentage"
        if self.daily_pnl <= -abs(self.stop_loss):
            return False, "stop loss reached"
        return True, "approved"

    def record_pnl(self, pnl: float) -> None:
        self.daily_pnl += pnl
