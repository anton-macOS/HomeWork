# Напишіть функцію-генератор з назвою count_down,
# яка отримує число і повертає зворотній відлік від цього числа до 0.
#
# Приклад використання:
# for i in count_down(10):
#     print(i)

# 10 9 8 7 6 5 4 3 2 1 0
def count_down(n):
    while n >= 0:
        yield n
        n -= 1


for i in count_down(10):
    print(i)