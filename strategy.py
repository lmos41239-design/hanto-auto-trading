def calculate_moving_average(prices):
    if not prices:
        raise ValueError("price list cannot be empty")
    return sum(prices) / len(prices)


def moving_average_strategy(current_price: int, price_history):
    """
    Generate a simple BUY / SELL / HOLD signal.

    Rule:
    - current price > moving average: BUY
    - current price < moving average: SELL
    - current price = moving average: HOLD
    """
    moving_average = calculate_moving_average(price_history)

    if current_price > moving_average:
        return "BUY", moving_average
    if current_price < moving_average:
        return "SELL", moving_average
    return "HOLD", moving_average
