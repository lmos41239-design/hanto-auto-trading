from datetime import datetime
from dataclasses import dataclass


@dataclass
class OrderResult:
    success: bool
    message: str
    stock_code: str
    side: str
    quantity: int
    price: int


class SimulationOrderAPI:
    """Simulated order executor. It does not send real orders."""

    def place_order(self, stock_code: str, side: str, quantity: int, price: int) -> OrderResult:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = (
            f"[{now}] Simulation order completed: "
            f"{side} {quantity} shares of {stock_code} at {price} KRW"
        )
        return OrderResult(True, message, stock_code, side, quantity, price)


class KISOrderAPI:
    """
    Placeholder for official mock trading order API.

    In the final API-connected version, connect this class to the official sample file:
    examples_llm/domestic_stock/order_cash/order_cash.py

    In mock trading mode, official order_cash examples generally use demo/mock trading settings.
    """

    def place_order(self, stock_code: str, side: str, quantity: int, price: int) -> OrderResult:
        raise NotImplementedError(
            "KISOrderAPI is not connected yet. Use SimulationOrderAPI first."
        )
