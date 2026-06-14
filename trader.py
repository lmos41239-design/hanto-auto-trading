from pathlib import Path
from market_api import SimulationMarketAPI, KISMarketAPI
from order_api import SimulationOrderAPI, KISOrderAPI
from strategy import moving_average_strategy


class AutoTrader:
    """Controller for the whole automatic trading process."""

    def __init__(self, settings):
        self.settings = settings

        if settings.mode == "kis_demo":
            self.market_api = KISMarketAPI()
            self.order_api = KISOrderAPI()
        else:
            self.market_api = SimulationMarketAPI()
            self.order_api = SimulationOrderAPI()

    def run_once(self):
        stock_code = self.settings.stock_code
        quantity = self.settings.quantity
        ma_window = self.settings.ma_window

        prices = self.market_api.get_recent_prices(stock_code)
        price_history = prices[-ma_window:]
        current_price = self.market_api.get_current_price(stock_code)
        signal, moving_average = moving_average_strategy(current_price, price_history)

        print(f"[CONFIG] mode={self.settings.mode}, stock_code={stock_code}, quantity={quantity}")
        print(f"[PRICE] current_price={current_price}, moving_average={moving_average}")
        print(f"[SIGNAL] {signal}")

        if signal in ["BUY", "SELL"]:
            order_result = self.order_api.place_order(stock_code, signal, quantity, current_price)
            print(f"[ORDER] {order_result.message}")
            self._save_log(order_result.message)
        else:
            message = f"HOLD signal for {stock_code}. No order was placed."
            print(f"[ORDER] {message}")
            self._save_log(message)

    def _save_log(self, message: str):
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        with open(log_dir / "trading_log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")
