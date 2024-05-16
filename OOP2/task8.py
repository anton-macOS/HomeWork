# Створіть функціонал для управління бібліотекою. Використовуйте всі набуті знання у ООП для
# кращого проектування, використовуйте атрибути класу та атрибути інстансу, classmethod та staticmethod,
# приватні та захищені атрибути і так далі. Бібліотека повинна мати такі класи: User, Book, Library, Customer,
# Employee.
#
# Клас Book повинен мати такі атрибути як: title, author, isbn, copies(У одній бібліотеці),
# total_copies(По всім бібліотекам). Клас повинен мати метод check_availability який буде перевіряти чи є книга
# у бібліотеці. Метод update_total_copies який буде оновлювати загальну кількість копій книжок коли вони будуть
# змінюватись. Метод який буде оновлювати кількість книжок у конкретній бібліотеці(змінювати параметр copies у
# інстанса).
# Також клас повинен мати метод validate_isbn який буде валідувати правильність isbn коду(ISBN 0-061-96436-0).
#
# Клас User повинен мати такі атрибути як name, user_id. ДАлі буде інфа про функціонал для Customer та Employee,
# де ви самі повинні розібратись які атрибути де мають бути та як це буде виглядати. Атрибути borrowed_books, salary,
# library. Методи для додавання книжки у бібліотеку та видаленню. Методи для взяття книжки з бібліотеки,
# та повернення.
#
# Клас Library буде мати поля books, users. Методи які дозволять зареєструвати юзера у бібліотеці,
# знайти книжку за isbn, та показати всі доступні книжки у бібліотеці.
#
# Важливо! Використовуйте все, атрибути класу, атрибути інстансу, клас методи та статик методи,
# проперті, приватні та протектед атрибути.
import re
from abc import ABC, abstractmethod


class BookInfo(ABC):
    _total_copies = 0

    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        BookInfo._total_copies += self.copies

    @abstractmethod
    def check_availability(self):
        pass

    @classmethod
    @abstractmethod
    def update_total_copies(cls, value):
        pass

    @abstractmethod
    def update_quantity(self):
        pass


class Book(BookInfo):
    def __init__(self, title, author, isbn, copies):
        super().__init__(title, author, isbn, copies)

    def check_availability(self):
        return self.copies

    @property
    def update_quantity(self):
        return self.copies

    @update_quantity.setter
    def update_quantity(self, value):
        if self.copies + value >= 0:
            self.copies += value
            Book.update_total_copies(value)
        else:
            raise 'Not enough books'

    @classmethod
    def update_total_copies(cls, value):
        cls._total_copies += value

    @staticmethod
    def validate_isbn(isbn):
        result = r'^\d{1}-\d{3}-\d{5}-\d{1}$'
        if re.fullmatch(result, isbn):
            return True
        else:
            raise 'Incorrect ISBN'

    def change_library_quantity(self, value):
        self.copies = value


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


class Customer(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def borrow_book(self, book,  value):
        if book.check_availability() >= value:
            book.update_quantity = -value
        else:
            raise 'Not enough books'

    def return_book(self, book, value):
        book.update_quantity = value


richard = Book('Richard', 'Gir', '0-061-96436-0', 1)
boom = Book('Boom', 'Gir', 101, 1)
richard.change_library_quantity(10)
print(richard.copies)
richard.change_library_quantity(5)
print(richard.copies)
print(richard.validate_isbn('0-061-96436-0'))
anton = Customer('Anton', 123)
anton.borrow_book(richard, 2)
print(richard.copies)
anton.borrow_book(richard, 3)
print(richard.copies)
anton.return_book(richard, 1)
print(richard.copies)






