# Напишіть рекурсивну функцію, яка приймає рядок та повертає його у зворотньому порядку.
#
# Приклад роботи:
# result = recursive_reverse("hello")   # olleh
def recursive_reverse(word):
    if len(word) <= 0:
        return word
    else:
        return word[-1] + recursive_reverse(word[:-1])


print(recursive_reverse('hello'))