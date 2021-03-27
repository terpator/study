"""
Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами.
"""


﻿class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"

    def volume(self):
        return self.x * self.y * self.z

    def add_boxes(box_1, box_2):
        return box_1.volume() + box_2.volume()


box_1 = Box(2, 3, 4)     
box_2 = Box(5, 6, 7)
print("Объем двух ящиков равен", Box.add_boxes(box_1, box_2))

