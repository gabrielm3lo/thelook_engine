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
    @timer
    def format_price(self, raw_price: Union[str, float, int]) -> float:
        try:
            price_str = str(raw_price)
            price_str = price_str.replace(",", ".")
            clean_price = round(float(price_str), 2)
            
            logger.debug(f"Converted: {raw_price} -> {clean_price}")
            
            return clean_price
        except ValueError as e:
            logger.error(f"Failed to format price: '{raw_price}'. Error: {e}")
            raise

if __name__ == "__main__":
    cleaner = TheLookCleaner()
    
    logger.info("Starting cleaning test battery...")
    price_1 = cleaner.format_price("1,99")
    logger.info(f"Test 1 result: {price_1}")