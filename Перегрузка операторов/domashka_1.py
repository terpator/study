"""
Создайте класс «Прямоугольник», у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по
площади. Также реализуйте методы сложения прямоугольников (площадь
суммарного прямоугольника должна быть равна сумме площадей
прямоугольников, которые вы складываете). Реализуйте методы
умножения прямоугольника на число n (это должно увеличить площадь
базового прямоугольника в n раз).
"""


﻿import numbers

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.s = self.width * self.height

    def __eq__(self, other):
        return self.s == other.s

    def __gt__(self, other):
        return self.s > other.s

    def __add__(self, other):
        self.s = self.s + other.s
        return self

    def __str__(self):
        return "Rectangle[width = {}, height = {}]".format(self.width, self.height)

    def __mul__(self, n):
        if isinstance(n, numbers.Real):
            self.s = self.s * n
            return self
        else:
            return NotImplemented


rec_1 = Rectangle(2, 3)
rec_2 = Rectangle(4, 5)
print("rec_1 < rec_2    ", rec_1 < rec_2)

rec_3 = rec_1 + rec_2
print("Площадь нового прямоугольника (+) равна", rec_3.s)

rec_3 = rec_1 * 4
print("Площадь нового прямоугольника (*4) равна", rec_3.s)
