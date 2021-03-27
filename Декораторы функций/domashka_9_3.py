"""
Предположим, в классе определен метод __str__, который возвращает
строку на основании класса. Создайте такой декоратор для этого метода,
чтобы полученная строка сохранялась в текстовый файл, имя которого
совпадает с именем класса, метод которого вы декорировали.
"""


﻿def decorator(f):
    def inner_func(*args, **kwargs):
        result = f(*args, **kwargs) 
        stream = open("SomeClass.txt", "w")
        stream.write(result)
        stream.close()
        return result
    return inner_func


class SomeClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @decorator
    def __str__(self):
        return f"SomeClass [x = {self.x}, y = {self.y}]"

class_1 = SomeClass(4, 6)
print(class_1)

