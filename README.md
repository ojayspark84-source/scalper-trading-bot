# Scalper Trading Bot

An automated scalper trading bot with configurable parameters for binary options and forex trading. Built with Python, featuring a modular architecture, risk management controls, and backtesting capabilities.

## Features

- 🤖 **Config-Driven Architecture**: Manage all bot parameters through YAML/JSON configuration
- 📊 **Scalping Strategy**: High-frequency trading strategy with customizable timeframes
- 🛡️ **Risk Management**: Built-in Martingale progression, stop-loss, and profit targets
- 📈 **Backtesting Engine**: Test strategies against historical data before live trading
- 🔔 **Notifications**: Multi-channel alerts (Blue, Silent, status monitoring)
- ⚙️ **CLI Interface**: Easy command-line control and monitoring
- 📝 **Logging & Analytics**: Detailed trade logs and performance metrics

## Project Structure

```
scalper-trading-bot/
├── config/
│   ├── default_config.yaml
│   └── strategies/
│       ├── scalper_strategy.yaml
│       └── martingale_config.yaml
├── src/
│   ├── bot.py
│   ├── strategy/
│   │   ├── __init__.py
│   │   ├── base_strategy.py
│   │   ├── scalper_strategy.py
│   │   └── signal_generator.py
│   ├── risk_management/
│   │   ├── __init__.py
│   │   ├── martingale.py
│   │   ├── position_manager.py
│   │   └── risk_calculator.py
│   ├── notifications/
│   │   ├── __init__.py
│   │   ├── notifier.py
│   │   └── channels/
│   │       ├── blue_alert.py
│   │       ├── silent_mode.py
│   │       └── status_monitor.py
│   ├── broker/
│   │   ├── __init__.py
│   │   ├── base_broker.py
│   │   ├── binary_broker.py
│   │   └── forex_broker.py
│   ├── backtest/
│   │   ├── __init__.py
│   │   ├── backtester.py
│   │   └── performance_analyzer.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── config_loader.py
│       └── data_handler.py
├── tests/
│   ├── test_strategy.py
│   ├── test_risk_management.py
│   ├── test_martingale.py
│   └── test_backtest.py
├── logs/
├── data/
│   └── historical/
├── main.py
├── backtest.py
├── requirements.txt
└── LICENSE
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ojayspark84-source/scalper-trading-bot.git
   cd scalper-trading-bot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

### 1. Configure Your Bot

Edit `config/default_config.yaml`:

```yaml
bot:
  name: "Scalper Bot"
  mode: "demo"  # demo or live
  broker: "binary"

trade_parameters:
  market: "forex"
  trade_type: "digits"
  contract_type: "both"
  candle_interval: 60  # seconds

initial_settings:
  initial_amount: 3
  win_amount: 3
  expected_profit: 700
  stop_loss: 100
  martingale_level: 1.05

run_once_at_start:
  notify_blue: true
  with_sound: false
  silent: false

notifications:
  blue_alert: enabled
  status_check_interval: 30
```

### 2. Run the Bot

```bash
python main.py --config config/default_config.yaml
```

### 3. Backtest Strategy

```bash
python backtest.py --config config/default_config.yaml --data data/historical/sample.csv
```

## Configuration Parameters

### Trade Parameters
- `market`: Currency/asset pair (forex, binary, crypto)
- `trade_type`: Type of trade (digits, touch, range)
- `contract_type`: Both, Call, or Put
- `candle_interval`: Timeframe in seconds (60, 300, 900, 3600)

### Initial Settings
- `initial_amount`: Starting stake (USD)
- `win_amount`: Target win per trade (USD)
- `expected_profit`: Expected daily profit (USD)
- `stop_loss`: Maximum loss threshold (USD)
- `martingale_level`: Multiplier for losing trades (1.05 = 5% increase)

### Risk Management
- Automatic position sizing based on account balance
- Stop-loss enforcement
- Profit-taking at expected levels
- Martingale progression limits

## Strategy Logic

### Scalper Strategy

The bot uses a multi-timeframe scalping approach:

1. **Signal Generation**: Analyzes price action on 1-minute candles
2. **Entry Points**: Identifies reversal/continuation patterns
3. **Risk/Reward**: Maintains 1:2 or better risk/reward ratio
4. **Exit Management**: Automated profit-taking and stop-loss
5. **Martingale Progression**: Increases stakes on losing streaks (configurable)

### Signal Types
- `BUY`: Price likely to go up
- `SELL`: Price likely to go down
- `HOLD`: No clear signal, avoid entry

## Notifications

### Blue Alert Mode
- High-priority notifications for trade signals
- Audio alerts on new positions
- Desktop notifications (Windows/macOS/Linux)

### Silent Mode
- Logging only, no audio/visual alerts
- Useful for server environments

### Status Monitor
- Periodic health checks
- Account balance updates
- Trade performance summaries

## Backtesting

Run historical backtests to validate strategy:

```bash
python backtest.py \
  --config config/default_config.yaml \
  --data data/historical/eurusd_2024.csv \
  --start-date 2024-01-01 \
  --end-date 2024-12-31 \
  --initial-balance 1000
```

## Performance Metrics

- **Win Rate**: Percentage of winning trades
- **Profit Factor**: Gross profit / Gross loss
- **Max Drawdown**: Largest peak-to-trough decline
- **Sharpe Ratio**: Risk-adjusted return
- **Total Return**: Overall profit/loss

## CLI Commands

```bash
# Run bot with default config
python main.py

# Run with custom config
python main.py --config my_config.yaml

# Backtest strategy
python backtest.py --config config/default_config.yaml --data data.csv

# Dry run (simulate without real trades)
python main.py --config config/default_config.yaml --dry-run

# Verbose logging
python main.py --log-level DEBUG

# Check bot status
python main.py --status
```

## Risk Warnings

⚠️ **DISCLAIMER**: Trading involves significant risk of loss. This bot is provided for educational and research purposes. Always:

- Test thoroughly in **demo mode** before live trading
- Start with small position sizes
- Monitor the bot regularly
- Have a clear risk management plan
- Never risk more than you can afford to lose
- Verify API credentials and broker authentication

## API Integration

Currently supports placeholder integrations for:
- Binary options brokers (IQ Option, Binomo, etc.)
- Forex brokers (MetaTrader 4/5, OANDA, etc.)

To integrate with a real broker:
1. Implement broker-specific API in `src/broker/`
2. Add authentication credentials to `.env`
3. Test in demo mode first

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Live broker API integrations
- [ ] Machine learning signal generation
- [ ] Multi-strategy portfolio management
- [ ] Web dashboard for monitoring
- [ ] Advanced risk analytics
- [ ] Mobile app integration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions, please open an [issue](https://github.com/ojayspark84-source/scalper-trading-bot/issues) on GitHub.

## Disclaimer

Trading is risky. This bot does not provide financial advice. Always conduct your own research and consult with a financial advisor before trading with real money.

---

**⚡ Scalper Trading Bot** - Automated, Configurable, and Educational Trading Strategy
