@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True) or {}
        print("WEBHOOK DATA:", data)

        # Required fields
        symbol = data.get("symbol")
        side = data.get("side")

        # Validate required strings
        if not symbol or not side:
            return jsonify({"error": "Missing symbol or side"}), 400

        # SL / TP safe parsing
        sl_raw = data.get("sl")
        tp_raw = data.get("tp")

        if sl_raw is None or tp_raw is None:
            return jsonify({"error": "Missing SL or TP"}), 400

        try:
            sl = float(sl_raw)
            tp = float(tp_raw)
        except (TypeError, ValueError):
            return jsonify({"error": "SL/TP must be numeric"}), 400

        # Optional fields (safe defaults)
        risk = float(data.get("risk", 1))
        qty = data.get("qty")

        # Log final parsed values
        print(f"PARSED → symbol={symbol}, side={side}, sl={sl}, tp={tp}, risk={risk}, qty={qty}")

        # ---- YOUR TRADING LOGIC HERE ----
        # place_order(symbol, side, qty, sl, tp)

        return jsonify({
            "status": "success",
            "symbol": symbol,
            "side": side,
            "sl": sl,
            "tp": tp
        })

    except Exception as e:
        print("WEBHOOK ERROR:", str(e))
        return jsonify({"error": "internal error"}), 500