from binance.exceptions import BinanceAPIException, BinanceRequestException
from .logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    logger.info(f"Attempting to place {order_type} {side} order for {quantity} {symbol}.")
    
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }
    
    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC" # Good 'Til Canceled

    try:
        # USDT-M Futures endpoint
        response = client.futures_create_order(**params)
        logger.info(f"Order successful. Order ID: {response.get('orderId')}")
        return response
        
    except BinanceAPIException as api_err:
        logger.error(f"Binance API Error: {api_err.message} (Code: {api_err.status_code})")
        raise Exception(f"Exchange Error: {api_err.message}")
    except BinanceRequestException as req_err:
        logger.error(f"Network Error: {req_err}")
        raise Exception("Network Error: Could not reach Binance API.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise Exception(f"System Error: {e}")