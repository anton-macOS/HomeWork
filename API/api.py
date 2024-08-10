import requests
api_key = '09858f80826ddc791facde5d'


class CurrencyConvertor:
    def __init__(self, key):
        self.key = key
        self.url = f'https://v6.exchangerate-api.com/v6/{self.key}'

    @staticmethod
    def check_response(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data

        except requests.exceptions.ConnectionError:
            return 'Ошибка соединения'

        except requests.exceptions.HTTPError:
            return 'HTTP ошибка'

        except requests.exceptions.Timeout:
            return 'Ошибка времени ожидания'

        except requests.exceptions.RequestException as e:
            return f'Произошла ошибка - {e}'

        except requests.exceptions.JSONDecodeError:
            return 'Вернулся не JSON'

        except Exception as e:
            return f'Ошибка - {e}'

    def get_exchange_info(self, from_curr, to_curr):
        url = f'{self.url}/pair/{from_curr}/{to_curr}'
        data = self.check_response(url)
        if isinstance(data, dict):
            if data['result'] == 'success':
                return f'Вот актальный курс на данный момент: {data['conversion_rate']}'
            elif data['result'] == 'error':
                return f'Что-то пошло не так! Вот код ошибки: {data['error-type']}'

    def convertor(self, from_curr, to_curr, value):
        url = f'{self.url}/pair/{from_curr}/{to_curr}/{value}'
        data = self.check_response(url)
        if isinstance(data, dict):
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
    