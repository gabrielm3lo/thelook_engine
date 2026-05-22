from src.cleaner import TheLookCleaner 
def test_format_price_round():
    cleaner = TheLookCleaner()
    nf_price = 10.55

    f_price = cleaner.format_price(nf_price)
    assert f_price == 10.55