# Напишіть рекурсивну функцію, буде конвертувати десяткове число у двійкове.
#
# Приклад роботи:
# result = recursive_dec_to_bin_converter(12)   # 1100

def recursive_dec_to_bin_converter(n):
    if n == 0:
        return ''
    else:
        return recursive_dec_to_bin_converter(n // 2) + str(n % 2)


print(recursive_dec_to_bin_converter(12))
