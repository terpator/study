"""
Создайте декоратор, который зарегистрирует декорируемый класс в
списке классов.
"""


﻿class_list = []

def dec(cls):
    class_list.append(cls)
    return cls

@dec
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

@dec
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(class_list)
