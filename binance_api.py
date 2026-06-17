from binance.client import Client

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

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