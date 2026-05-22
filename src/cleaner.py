class TheLookCleaner: 
    def format_price(self,raw_price):
        price_str = str(raw_price)
        price_str = price_str.replace(",", ".")
        return round(float(raw_price), 2)
