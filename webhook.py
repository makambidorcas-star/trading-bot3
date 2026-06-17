from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Works for both JSON and raw text payloads from TradingView
        data = request.get_json(silent=True)

        if data is None:
            data = request.data.decode("utf-8")
            print("RAW WEBHOOK:", data)
            return jsonify({"status": "received_raw"}), 200

        print("WEBHOOK:", data)

        # direct pass-through (no filtering logic)
        symbol = data.get("symbol")
        side = data.get("side")
        sl = data.get("sl")
        tp = data.get("tp")
        qty = data.get("qty")
        risk = data.get("risk")

        print(f"EXEC → {symbol} {side} SL={sl} TP={tp} qty={qty} risk={risk}")

        # EXECUTE HERE
        # place_order(symbol, side, qty, sl, tp)

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        print("WEBHOOK ERROR:", str(e))
        return jsonify({"error": "server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)