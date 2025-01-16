# 1. SyntaxError (SINTEKS XATOLIK)
# if True print("Hello")  # Komment qilingan, ochib ishlatishingiz mumkin

# 2. EOL va EOF xatoliklari
# print("Hello  # EOL (Qator oxirida yopilmagan string)
# def my_function():      # EOF (Funktsiya ochilgan, lekin yopilmagan)
#     print("Hello")

# 3. IndentationError (JOY TASHLASHDA XATOLIK)
# def my_function():
# print("Hello")  # To'g'ri joy tashlanmagan

# 4. ValueError
# int("abc")  # "abc" son emas, shuning uchun ValueError

# 5. TypeError
# "5" + 5  # Matnni son bilan qo'shib bo'lmaydi

# 6. NameError
# print(unknown_variable)  # unknown_variable aniqlanmagan

# 7. IndexError
# my_list = [1, 2, 3]
# print(my_list[5])  # Indeks diapazondan tashqarida

# 8. ZeroDivisionError
# result = 10 / 0  # Nolga bo'lish taqiqlangan
