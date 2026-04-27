# Primetrade.ai - Binance Futures Trading Bot

A modular, decoupled Python application that interfaces with the Binance Futures Testnet (USDT-M) to execute MARKET and LIMIT orders.


## Directory Structure
```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py         # Binance client wrapper
│   ├── orders.py         # Order placement logic
│   ├── validators.py     # Input validation
│   └── logging_config.py # Logging setup
│
├── cli.py                # Main CLI entry point
├── ui.py                 # Bonus Streamlit UI
├── requirements.txt
├── .env                  # Your API keys (DO NOT COMMIT THIS TO GITHUB)
└── README.md
```

## Architecture
The project strictly separates the business/API logic from the presentation layer. 
- `bot/`: Contains the Binance client wrapper, order execution logic, and input validators.
- `cli.py`: A command-line interface.
- `ui.py`: A lightweight Web UI (Bonus).

## Setup Instructions

1. **Clone/Extract the repository**
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt


How to Run Examples
1. Command Line Interface (CLI)
Run cli.py passing the required arguments.

Example: MARKET Order
```Bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
```
Example: LIMIT Order

```Bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.05 --price 3500
```
2. Streamlit UI (Bonus)
To use the graphical interface, run:

```Bash
streamlit run ui.py
```