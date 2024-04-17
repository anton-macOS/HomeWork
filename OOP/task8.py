# Створіть клас Library, який зберігає книги (у вигляді списку екземплярів класу Book).
# Реалізуйте __len__ для повернення кількості книг у бібліотеці та __getitem__ для доступу
# до книги за заданим індексом.
#
# Приклад використання:
# b1 = Book("Title1", "Author1")
# b2 = Book("Title2", "Author2")
# b3 = Book("Title3", "Author3")
# library = Library([b1, b2, b3])
# print(len(library))
# print(library[2])
class Book:
    def __init__(self, title, author):
        self.title = title
        self. author = author

    def __repr__(self):
        return f'Book is {self.title}, {self.title}'

    def __str__(self):
        return self.__repr__()


class Library:
    def __init__(self, book):
        self.book = book

    def __len__(self):
        return len(self.book)

    def __getitem__(self, item):
        return self.book[item]


b1 = Book("Title1", "Author1")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")
library = Library([b1, b2, b3])
print(len(library))
print(library[2])
