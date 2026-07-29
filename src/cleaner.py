import time
import logging
from functools import wraps
from typing import Union

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logger.info(f"[PERFORMANCE] Function '{func.__name__}' executed in {run_time:.6f} seconds.")
        return result
    return wrapper_timer

class TheLookCleaner:
    def __init__(self, currency_symbol: str = "$", decimal_separator: str = "."):
        self.currency_symbol = currency_symbol
        self.decimal_separator = decimal_separator

        logger.info(
            f"TheLookCleaner initialized | Currency: '{self.currency_symbol}' | Decimal Separator: '{self.decimal_separator}'"
        )

    @timer
    def format_price(self, raw_price: Union[str, float, int], default_on_error: float = 0.0) -> float:
        if raw_price is None:
            logger.warning("Received raw_price is None. Returning default value.")
            return default_on_error

        try:
            price_str = str(raw_price).strip()
            price_str = price_str.replace(self.currency_symbol, "").replace("R$", "").replace("$", "").strip()

            if self.decimal_separator == ".":
                if "," in price_str and "." in price_str:
                    price_str = price_str.replace(".", "").replace(",", ".")
                else:
                    price_str = price_str.replace(",", ".")

            clean_price = round(float(price_str), 2)
            logger.debug(f"Successfully converted: '{raw_price}' -> {clean_price}")
            return clean_price

        except (ValueError, TypeError) as e:
            logger.error(f"Failed to format price: '{raw_price}'. Error: {e}. Returning default: {default_on_error}")
            return default_on_error

if __name__ == "__main__":
    logger.info("=== Starting Test Battery ===")

    cleaner_us = TheLookCleaner(currency_symbol="$", decimal_separator=".")

    test_items = ["1,99", "R$ 50,00", "$ 120.50", " 1.250,90 ", None, "invalid_text"]

    for item in test_items:
        result = cleaner_us.format_price(item)
        logger.info(f"Input: {str(item):<15} | Output: {result}")