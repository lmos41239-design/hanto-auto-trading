class SimulationMarketAPI:
    """Market price provider for safe local testing."""

    def get_recent_prices(self, stock_code: str):
        # Example prices. In a real project, these are replaced by KIS Open API price data.
        return [71000, 71500, 72000, 72500, 73000, 73500]

    def get_current_price(self, stock_code: str) -> int:
        return self.get_recent_prices(stock_code)[-1]


class KISMarketAPI:
    """
    Placeholder for official Korea Investment Securities Open API price inquiry.

    In the final API-connected version, connect this class to the official sample file:
    examples_llm/domestic_stock/inquire_price/inquire_price.py
    """

    def get_recent_prices(self, stock_code: str):
        raise NotImplementedError(
            "KISMarketAPI is not connected yet. Use SimulationMarketAPI first."
        )

    def get_current_price(self, stock_code: str) -> int:
        raise NotImplementedError(
            "KISMarketAPI is not connected yet. Use SimulationMarketAPI first."
        )
