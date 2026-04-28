import streamlit as st
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs

st.set_page_config(page_title="Trading Bot Dashboard", page_icon="📈")
st.title("📈 Binance Futures Bot")

with st.form("order_form"):
    col1, col2 = st.columns(2)
    with col1:
        symbol = st.text_input("Symbol", value="BTCUSDT").upper()
        side = st.selectbox("Side", ["BUY", "SELL"])
        quantity = st.number_input("Quantity", min_value=0.001, format="%.3f")
    with col2:
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        price = st.number_input("Price (Required for LIMIT)", min_value=0.0, format="%.2f")
    
    submitted = st.form_submit_button("Place Order")

if submitted:
    try:
        # Re-using the exact same logic as the CLI
        sym, sde, typ, qty, prc = validate_inputs(symbol, side, order_type, quantity, price if order_type == "LIMIT" else None)
        client = get_client()
        
        with st.spinner("Placing order..."):
            response = place_order(client, sym, sde, typ, qty, prc)
            
        st.success(" Order Placed Successfully!")
        st.json({
            "Order ID": response.get('orderId'),
            "Status": response.get('status'),
            "Executed Qty": response.get('executedQty'),
            "Avg Price": response.get('avgPrice', 'N/A')
        })
            
    except ValueError as ve:
        st.error(f"Validation Error: {ve}")
    except Exception as e:
        st.error(f"Failed: {e}")