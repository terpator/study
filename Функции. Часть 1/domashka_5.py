"""
Напишите функцию, которая вернет количество слов в строке текста.
"""


def words_calc(text):
    somelist = text.split(" ")
    return len(somelist)

text = input("Введите строку: ")
if text == "":
    print("Строка пустая")
else:
    print("Количество слов в строке: ", words_calc(text))
