import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
from .logging_config import setup_logger

logger = setup_logger()
load_dotenv()

def get_client() -> Client:
    # 1. Fetch credentials
    api_key = os.getenv("BINANCE_API_KEY")
    # Using 'BINANCE_API_SECRET' based on your provided check logic
    api_secret = os.getenv("BINANCE_API_SECRET") 
    
    # 2. Check if keys exist
    if not api_key or not api_secret:
        logger.error("API credentials missing in .env file.")
        raise ValueError("Missing Binance API credentials. Check your .env file.")
        
    try:
        # 3. Initialize the client
        logger.info("Initializing Binance Futures Testnet client.")
        client = Client(api_key, api_secret, testnet=True)
        
        # 4. Immediate Connection Check (Verification)
        # We call futures_account_balance() to ensure the keys actually work
        balance = client.futures_account_balance()
        logger.info("✅ Connection verified! Successfully retrieved Futures balance.")
        
        # Optional: Print balance to console for immediate feedback
        print(f"Connected to Testnet! Account Balance: {balance}")
        
        return client

    except BinanceAPIException as e:
        logger.error(f"❌ Binance API Error during initialization: {e.message}")
        raise
    except Exception as e:
        logger.error(f"⚠️ Unexpected error connecting to Binance: {e}")
        raise