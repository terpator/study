"""
Создайте декоратор класса с параметром. Параметром должна быть
строка, которая должна дописываться (слева) к результату работы метода
__str__.
"""


﻿def dec(text):
    def inner(cls):
        def __str__(self):
            return text + " " + str(self.__str__)
        cls.__str__ = __str__
        return cls
    return inner
    

@dec("Some text")
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_1 = Cat("Vaska", 12)
print(cat_1)
