import requests

api_key = '09858f80826ddc791facde5d'
weather_api = '5fffd2cc778042e0af3154944241908'


class ApiService:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, endpoint='', http_method='get', expected_format='json'):
        valid_methods = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'connect', 'trace']
        url = f'{self.base_url}/{endpoint}'
        if http_method in valid_methods:
            try:
                response = requests.request(http_method, url)
                return self.validate_response(response, expected_format)

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

        else:
            raise ValueError(f'Не верный формат HTTP: {expected_format}')

    @staticmethod
    def validate_response(response, expected_format):
        if response.status_code == 200:
            if expected_format == 'json':
                return response.json()
            elif expected_format == 'text':
                return response.text
            else:
                raise ValueError(f'Не верный формат: {expected_format}')
        else:
            return response.raise_for_status()


class Convertor(ApiService):
    def __init__(self, base_url):
        super().__init__(base_url)

    def check_data(self, endpoint):
        data = self.send_request(endpoint, 'get', 'json')
        if isinstance(data, dict):
            if data['result'] == 'success':
                return data
            elif data['result'] == 'error':
                return f'Что-то пошло не так! Код ошибки: {data['error-type']}'

    def get_exchange_info(self, from_curr, to_curr):
        endpoint = f'pair/{from_curr}/{to_curr}/'
        data = self.check_data(endpoint)
        return f'Вот актальный курс на данный момент: {data['conversion_rate']}'

    def convert(self, from_curr, to_curr, value):
        endpoint = f'pair/{from_curr}/{to_curr}/{value}'
        data = self.check_data(endpoint)
        return (f'Актуальный курс обмена - {data['conversion_rate']}, '
                f'вы получите на руки - {data['conversion_result']}')


convertor = Convertor(f'https://v6.exchangerate-api.com/v6/{api_key}')


# weather = ApiService(f'http://api.weatherapi.com/v1/')
# print(weather.send_request(f'current.json?key={weather_api}&q=London&aqi=no',
#                            'get', 'json'))
#
# news = ApiService('https://ua.korrespondent.net')
# print(news.send_request(expected_format='text'))

question = input('курс или конвертация? ').lower()

if question == 'курс':
    first_curr = input('Какая у Вас валюта? ').upper()
    second_curr = input('В какую валюту конвертировать? ').upper()
    print(convertor.get_exchange_info(first_curr, second_curr))

elif question == 'конвертация':
    first_curr = input('Какую валюту отдаете? ').upper()
    amount = float(input(f'Какая сумма к обмену в {first_curr}? '))
    second_curr = input('В какую валюту желаете обменять? ').upper()
    print(convertor.convert(first_curr, second_curr, amount))
