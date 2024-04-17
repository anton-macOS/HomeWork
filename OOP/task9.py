# Створіть клас Logger, який буде логувати у консоль будь яке повідомлення.
# Цей клас буде приймати рядок як log_level та мати метод __call__ який буде
# виводити у консоль повідомлення у форматі {log_level}: {message}.
#
# Приклад використання:
# logger = Logger("Info")
# logger("Something happened!")   # Info: Something happened!
class Logger:
    def __init__(self, log_level):
        self.log_level = log_level

    def __call__(self, message):
        print(f'{self.log_level}: {message}')


logger = Logger("Info")
logger("Something happened!")   # Info: Something happened!
