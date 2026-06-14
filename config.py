from dataclasses import dataclass
from pathlib import Path
import os


def _load_dotenv(path: str = ".env") -> None:
    """Small .env loader so the project can run even without python-dotenv."""
    env_path = Path(path)
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


@dataclass
class Settings:
    mode: str = "simulation"          # simulation / kis_demo
    stock_code: str = "005930"        # Samsung Electronics
    quantity: int = 1
    ma_window: int = 5
    app_key: str = ""
    app_secret: str = ""
    account_no: str = ""
    account_product_code: str = "01"


def load_settings() -> Settings:
    _load_dotenv()
    return Settings(
        mode=os.getenv("MODE", "simulation"),
        stock_code=os.getenv("STOCK_CODE", "005930"),
        quantity=int(os.getenv("QUANTITY", "1")),
        ma_window=int(os.getenv("MA_WINDOW", "5")),
        app_key=os.getenv("APP_KEY", ""),
        app_secret=os.getenv("APP_SECRET", ""),
        account_no=os.getenv("ACCOUNT_NO", ""),
        account_product_code=os.getenv("ACCOUNT_PRODUCT_CODE", "01"),
    )
