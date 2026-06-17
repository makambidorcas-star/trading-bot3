import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)


def place_order(symbol, side, qty, sl=None, tp=None):
    try:
        print("=== ORDER FUNCTION HIT ===")

        order_side = Client.SIDE_BUY if side.upper() == "BUY" else Client.SIDE_SELL

        order = client.create_order(
            symbol=symbol,
            side=order_side,
            type=Client.ORDER_TYPE_MARKET,
            quantity=qty
        )

        print("ORDER RESPONSE:", order)

        return order

    except Exception as e:
        print("BINANCE ERROR:", e)
        return None
