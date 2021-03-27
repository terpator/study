"""
Написать программу, которая считывает 5-ти значное число с
клавиатуры и выводит цифры, из которого оно состоит.
Например : Считывается число 54698
Выводится:
5
4
6
9
8
"""





number = int(input("Enter number:"))
digit_1 = number // 10000
digit_2 = number % 10000 // 1000
digit_3 = number % 1000 // 100
digit_4 = number % 100 // 10
digit_5 = number % 10 // 1

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
print(digit_5)
