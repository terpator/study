"""
Считайте строку, которая будет представлять имя человека, введенное с
клавиатуры. Проверьте эту строку на валидность. Имеется в виду, что например, в
имени человека не может быть цифр, оно должно начинаться с большой буквы, за
которой должны следовать маленькие.
"""


text = input("Введите имя:")
if text.isalpha() != True:
     print("Имя содержит символы кроме букв!")
elif text.istitle() != True:
     print("Имя не начинается с большой буквы!")
else:
     print("Имя - ОК")

