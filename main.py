from __future__ import annotations

import argparse
import logging

from src.broker.paper_broker import PaperBroker
from src.risk_management.martingale import Martingale
from src.risk_management.risk_manager import RiskManager
from src.strategy.models import Candle
from src.strategy.scalper_strategy import ScalperStrategy
from src.utils.config_loader import load_config
from src.utils.logger import configure_logging


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the scalper bot in safe paper mode")
    parser.add_argument("--config", default="config/default_config.yaml")
    parser.add_argument("--log-level", default="INFO")
    parser.add_argument("--dry-run", action="store_true", help="validate configuration only")
    args = parser.parse_args()
    configure_logging(args.log_level)
    config = load_config(args.config)
    logger = logging.getLogger("scalper")
    strategy = ScalperStrategy(**{key: config.get("strategy", key) for key in
                                  ("fast_ema", "slow_ema", "rsi_period", "rsi_oversold", "rsi_overbought", "minimum_confidence")})
    martingale = Martingale(config.get("initial_settings", "initial_amount", default=1.0),
                            config.get("initial_settings", "martingale_level", default=1.0),
                            config.get("initial_settings", "max_martingale_steps", default=3))
    risk = RiskManager(config.get("risk", "starting_balance", default=1000.0),
                       config.get("initial_settings", "stop_loss", default=100.0),
                       config.get("risk", "max_daily_loss", default=100.0),
                       config.get("risk", "max_trade_risk_percent", default=1.0))
    if args.dry_run:
        logger.info("Configuration valid for %s", config.get("bot", "name", default="Scalper Bot"))
        return
    logger.info("Starting in %s mode; no live broker is configured", config.get("bot", "mode", default="demo"))
    logger.info("Strategy=%s/%s, stake=%.2f, balance=%.2f", strategy.fast_ema, strategy.slow_ema,
                martingale.next_stake(), risk.starting_balance)
    PaperBroker(risk.starting_balance)
    logger.info("Paper broker initialized. Supply a market-data adapter to begin simulation.")


if __name__ == "__main__":
    main()
