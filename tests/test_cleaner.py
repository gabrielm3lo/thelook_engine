import pytest
from src.cleaner import TheLookCleaner 

def test_format_price_round():
    cleaner = TheLookCleaner()
    nf_price = 10.55

    f_price = cleaner.format_price(nf_price)
    assert f_price == 10.55

def test_format_price_should_raise_error_for_invalid_text():
    cleaner = TheLookCleaner()
    inv_price = "dez reais"
    with pytest.raises(ValueError):
        cleaner.format_price(inv_price)