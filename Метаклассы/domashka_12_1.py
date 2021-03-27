"""
Реализуйте метакласс, который обладает следующим функционалом: при
его использовании в файл с заранее определенным названием нужно
сохранить имя класса и список его полей.
"""


﻿class MetaCls(type):

    def __init__(self_class, class_name, super_classes, class_atr):
        f = open("log.txt", "w")
        result = "Имя класса:\n" + class_name + "\n\n"
        result += "Список его полей:"+ "\n"
        for field_name in class_atr:
            result += field_name + " = " + str(class_atr[field_name]) + "\n"
        f.write(result)
        f.close()
        return type.__init__(self_class, class_name, super_classes, class_atr)

    
class Cat(metaclass=MetaCls):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    

cat_1 = Cat("Umka", 9)
print("Результат работы программы - в файле 'log.txt'")
