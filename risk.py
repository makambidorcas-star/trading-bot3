RISK_PER_TRADE = 0.003  # 0.3%

def calculate_position_size(balance_usdt, entry_price, stop_loss_price):
    risk_amount = balance_usdt * RISK_PER_TRADE

    stop_distance = abs(entry_price - stop_loss_price)

    if stop_distance == 0:
        return 0

    position_size = risk_amount / stop_distance

    return position_size