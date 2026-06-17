from binance.client import Client
from config import API_KEY, SECRET_KEY

client = Client(API_KEY, SECRET_KEY)

def place_order(symbol, side, quantity):
    try:
        print(f"[TRADE] {side} {quantity} {symbol}")

        order = client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        return order

    except Exception as e:
        print("Order error:", e)
        return None


def get_balance(asset="USDT"):
    try:
        balance = client.get_asset_balance(asset=asset)
        return float(balance["free"])
    except Exception as e:
        print("Balance error:", e)
        return 0


def get_price(symbol):
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
    except Exception as e:
        print("Price error:", e)
        return 0