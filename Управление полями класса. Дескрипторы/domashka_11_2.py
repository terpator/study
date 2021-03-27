"""
Реализуйте функционал, который будет запрещать установку полей класса
любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
попытаться присвоить, например, строку, то должно быть возбужденно
исключение.
"""


﻿class AppleTree:

    def __init__(self, __age):
        self.__age = __age
        
    age = property()

    @age.getter
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) == int:
            self.__age = value
        else:
            raise AttributeError("This field is integer type")
    
    def __str__(self):
        return f"AppleTree [age = {self.__age}]"
    

apple_tree_1 = AppleTree(50)
print(apple_tree_1)
print()
apple_tree_1.age = 20
print(apple_tree_1)
print()
apple_tree_1.age = "Very high!"


