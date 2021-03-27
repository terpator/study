"""
Реализуйте
свойство
класса,
которое
обладает
следующим
функционалом: при установки значения этого свойства в файл с заранее
определенным названием должно сохранятся время (когда устанавливали
значение свойства) и установленное значение.
"""


﻿import time

class AppleTree:

    def __init__(self, __age, hight):
        self.__age = __age
        self.hight = hight

    age = property()

    @age.getter
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        f = open("log.txt", "w")
        named_tuple = time.localtime()
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        line = str(time_string) + "   new value: " + str(value)
        f.write(line)
        f.close()
        self.__age = value
    
    def __str__(self):
        return f"AppleTree [age = {self.__age}, hight = {self.hight}]"
    

apple_tree_1 = AppleTree(50, 5)
print(apple_tree_1)
print()
apple_tree_1.age = 20
print(apple_tree_1)
print()


