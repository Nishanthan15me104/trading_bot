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
2. **Create and activate the Environment** - thsi for powershell
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. **Install Dependencies:**
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

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

## Challenges
- Fix 1: The recvWindow Error (Time Sync) : Updated bot/client.py to tell the library to automatically adjust for this time difference.
- Fix 2: The UnicodeEncodeError : Updated bot/logging_config.py to force UTF-8 encoding.


## Improvements 

- The Production/Institutional Standard: Real trading firms don't use a software offset. They use NTP (Network Time Protocol) or PTP (Precision Time Protocol) to sync their entire operating system's clock to atomic clocks with microsecond accuracy