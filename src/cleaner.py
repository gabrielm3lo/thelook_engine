from typing import Union

class TheLookCleaner:
    def format_price(self, raw_price: Union[str, float, int]) -> float:
        """
        Limpa e formata o preço bruto de um produto.
        Aceita números ou strings (padrão US com '.' ou BR com ',').
        Garante o retorno de um float com 2 casas decimais.
        """
        price_str = str(raw_price)
        price_str = price_str.replace(",", ".")
        return round(float(price_str), 2)