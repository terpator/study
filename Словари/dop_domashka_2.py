"""
Напишите программу, которая переведет целое число (от 1 до 100) из римской
записи в обычные цифры.
Например: XXII -> 22
Подробнее: https://en.wikipedia.org/wiki/Roman_numerals
"""


number = int(input("Введите число от 1 до 100: "))
digits = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds = ["", "C"]
if number < 1 or number > 100:
     print("Введите корректное число!")
else:
     h = hundreds[number // 100 % 10]
     t = tens[number // 10 % 10]
     d = digits[number % 10]
     print("Запись Вашего числа римскими цифрами: ",h+t+d)
