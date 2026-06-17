from flask import Flask, request, jsonify
from binance_api import place_order, get_balance, get_price
from risk import calculate_position_size

app = Flask(__name__)

SECRET_KEY = "amsee123"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Signal received:", data)

    # security check
    key = data.get("key")
    if key != SECRET_KEY:
        print("Invalid webhook key")
        return {"status": "rejected_security"}, 403

    action = data.get("action")
    symbol = data.get("symbol")

    entry = data.get("entry")
    sl = data.get("sl")
    tp = data.get("tp")

    # validation
    if entry is None or sl is None:
        print("Missing entry or SL → reject trade")
        return {"status": "rejected_missing_data"}, 200

    entry = float(entry)
    sl = float(sl)

    balance = get_balance("USDT")

    qty = calculate_position_size(balance, entry, sl)

    if qty <= 0:
        return {"status": "invalid_size"}, 200

    if action == "BUY":
        place_order(symbol, "BUY", qty)

    elif action == "SELL":
        place_order(symbol, "SELL", qty)

    return jsonify({
        "status": "executed",
        "symbol": symbol,
        "qty": qty,
        "entry": entry,
        "sl": sl,
        "tp": tp
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)