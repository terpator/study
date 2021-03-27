"""
1) Создайте ABC класс с абстрактным методом проверки целого числа на
простоту. Т.е., если параметром этого метода является целое число и оно
простое, то метод должен вернуть True, а в противном случае False.

2) Создайте класс его наследующий.

3) Создайте класс, который не наследует пользовательский ABC класс, но
обладает нужным методом. Зарегистрируйте его в качестве виртуального
подкласса.

4) Проверьте работоспособность проекта.
"""


﻿import abc

class PrimeNumberValidator(abc.ABC):

    @abc.abstractmethod
    def validate(self, number):
        "Validate number"

class NumberValidator(PrimeNumberValidator):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def validate(self, number):
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    

class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    
validator_1 = NumberValidator(32)
print("validator_1 is instance of PrimeNumberValidator: ", isinstance(validator_1, PrimeNumberValidator))
PrimeNumberValidator.register(Box)
box_1 = Box(1, 2, 3)
print("box_1 is instance of PrimeNumberValidator:", isinstance(box_1, PrimeNumberValidator))
