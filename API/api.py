import requests
api_key = '09858f80826ddc791facde5d'


class CurrencyConvertor:
    def __init__(self, key):
        self.key = key
        self.url = f'https://v6.exchangerate-api.com/v6/{self.key}'

    def get_exchange_info(self, from_curr, to_curr):
        responce = requests.get(f'{self.url}/pair/{from_curr}/{to_curr}')
        data = responce.json()
        if data['result'] == 'success':
            return f'Вот актальный курс на данный момент: {data['conversion_rate']}'
        elif data['result'] == 'error':
            return f'Что-то пошло не так! Вот код ошибки: {data['error-type']}'

    def convertor(self, from_curr, to_curr, value):
        responce = requests.get(f'{self.url}/pair/{from_curr}/{to_curr}/{value}')
        data = responce.json()
        if data['result'] == 'success':
            return (f'Актуальный курс обмена - {data['conversion_rate']}, '
                    f' вы получите на руки - {data['conversion_result']}')
        elif data['result'] == 'error':
            return f'Что-то пошло не так! Вот код ошибки: {data['error-type']}'


convertor = CurrencyConvertor(api_key)

question = input('курс или конвертация? ').lower()

if question == 'курс':
    first_curr = input('Какая у Вас валюта? ').upper()
    second_curr = input('В какую валюту конвертировать? ').upper()
    print(convertor.get_exchange_info(first_curr, second_curr))

elif question == 'конвертация':
    first_curr = input('Какую валюту отдаете? ').upper()
    amount = float(input(f'Какая сумма к обмену в {first_curr}? '))
    second_curr = input('В какую валюту желаете обменять? ').upper()
    print(convertor.convertor(first_curr, second_curr, amount))
    