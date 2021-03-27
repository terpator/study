"""
Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.
"""


﻿class MyDescriptor:

    def __init__(self, color):
        self.color = color
    
    def __get__(self, instance_self, instance_class):
        return self.color

    def __set__(self, instance_self, value):
        raise AttributeError("Setting this field is forbidden")

    def __delete__(self, instance_self):
        raise AttributeError("Removing this field is forbidden")


class Apple:

    color = MyDescriptor("Green")

    def __str__(self):
        return f"Apple [color = {self.color}]"
    

apple_1 = Apple()
print(apple_1)
print()
apple_1.color = "Black"
