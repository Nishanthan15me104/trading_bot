import os
import time
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
from .logging_config import setup_logger

logger = setup_logger()
load_dotenv()

def get_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET") 
    
    if not api_key or not api_secret:
        logger.error("API credentials missing in .env file.")
        raise ValueError("Missing Binance API credentials.")
        
    try:
        # Initialize
        client = Client(api_key, api_secret, testnet=True)
        
        # FIX: Sync time to avoid 'recvWindow' errors
        server_time = client.get_server_time()
        client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)
        
        # Verify connection
        client.futures_account_balance()
        logger.info("Connection verified successfully.")
        return client

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise