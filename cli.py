import argparse
import sys
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs

def main():
    parser = argparse.ArgumentParser(description="Primetrade.ai Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Amount to trade")
    parser.add_argument("--price", type=float, help="Price (required if type is LIMIT)", default=None)

    args = parser.parse_args()

    print("\n--- Order Request Summary ---")
    print(f"Symbol:   {args.symbol.upper()}")
    print(f"Side:     {args.side.upper()}")
    print(f"Type:     {args.type.upper()}")
    print(f"Quantity: {args.quantity}")
    if args.type.upper() == "LIMIT":
        print(f"Price:    {args.price}")
    print("-----------------------------\n")

    try:
        # 1. Validate
        sym, side, ord_type, qty, price = validate_inputs(
            args.symbol, args.side, args.type, args.quantity, args.price
        )
        
        # 2. Get Client
        client = get_client()
        
        # 3. Execute
        response = place_order(client, sym, side, ord_type, qty, price)
        
        # 4. Print Success
        print("✅ SUCCESS: Order Placed Successfully!")
        print(f"Order ID:     {response.get('orderId')}")
        print(f"Status:       {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price:    {response.get('avgPrice', 'N/A')}\n")

    except ValueError as ve:
        print(f"❌ VALIDATION ERROR: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ FAILURE: {e}")
        print("Check bot.log for more details.")
        sys.exit(1)

if __name__ == "__main__":
    main()