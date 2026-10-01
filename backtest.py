from __future__ import annotations

import argparse

from src.backtest.backtester import Backtester
from src.strategy.scalper_strategy import ScalperStrategy
from src.utils.config_loader import load_config
from src.utils.data_handler import load_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Backtest the scalper strategy")
    parser.add_argument("--config", default="config/default_config.yaml")
    parser.add_argument("--data", required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    strategy = ScalperStrategy(**{key: config.get("strategy", key) for key in
                                  ("fast_ema", "slow_ema", "rsi_period", "rsi_oversold", "rsi_overbought", "minimum_confidence")})
    result = Backtester(strategy, config.get("initial_settings", "initial_amount", default=1.0),
                        starting_balance=config.get("risk", "starting_balance", default=1000.0)).run(load_csv(args.data))
    print(f"Balance: {result.starting_balance:.2f} -> {result.ending_balance:.2f}")
    print(f"Trades: {result.trades}, wins: {result.wins}, losses: {result.losses}, win rate: {result.win_rate:.2%}")


if __name__ == "__main__":
    main()
