from datetime import datetime, timezone

from src.strategy.models import Candle, Signal
from src.strategy.scalper_strategy import ScalperStrategy


def test_strategy_holds_without_history():
    candle = Candle(datetime.now(timezone.utc), 1, 1, 1, 1)
    assert ScalperStrategy().generate_signal([candle]).signal == Signal.HOLD
