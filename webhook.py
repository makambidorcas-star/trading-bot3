from flask import Flask, request, jsonify
from binance_api import place_order, get_balance
from risk import calculate_position_size

app = Flask(__name__)

SECRET_KEY = "amsee123"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Signal received:", data)

    if data.get("key") != SECRET_KEY:
        return {"status": "rejected"}, 403

    action = data.get("action")
    symbol = data.get("symbol")
    entry = float(data.get("entry"))
    sl = float(data.get("sl"))

    balance = get_balance("USDT")
    qty = calculate_position_size(balance, entry, sl)

    if qty <= 0:
        return {"status": "invalid_size"}, 200

    if action.upper() == "BUY":
        place_order(symbol, "BUY", qty)
    elif action.upper() == "SELL":
        place_order(symbol, "SELL", qty)

    return jsonify({
        "status": "executed",
        "symbol": symbol,
        "qty": qty
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)