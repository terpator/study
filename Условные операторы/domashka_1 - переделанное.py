"""
Написать программу, которая считает 4 числа c клавиатуры и выведет на экран
самое большое из них.
"""


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))
number4 = int(input("Enter number4: "))
max_number = number1
if number2 > max_number:
    max_number = number2
if number3 > max_number:
    max_number = number3
if number4 > max_number:
    max_number = number4
print("Максимальное число равно ", max_number)
