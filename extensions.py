import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        values = quote, base, amount
        if len(values) > 3:
            raise ConvertionException('Слишком много параметров')

        if quote == base:
            raise ConvertionException(f'Невозможно перевсти одинаковые валюты{base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать колличество {amount}')
        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/5f25f757ec8d0bc29337395a/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate']
        return total_base