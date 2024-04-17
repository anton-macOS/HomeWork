# Розробіть клас Book, атрибутами якого є title та author.
# Реалізуйте __eq__ для перевірки рівності на основі назви та автора та __ne__ для перевірки нерівності.
#
# Приклад використання:
# book1 = Book("Title1", "Author1")
# book2 = Book("Title2", "Author2")
# print(book1 == book2)
# print(book1 == book2)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # def __ne__(self, other):
    #     return self.title != other.title and self.author != other.author


book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")
print(book1 == book2)
print(book1 == book2)
print(book1 != book2)
print(book1 != book2)