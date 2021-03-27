"""
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
"""


﻿class CallCount:
    
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        result = self.f(*args, **kwargs)    
        self.count += 1
        return result
    
        
@CallCount
def summa(a, b):
    return a + b

print(summa(3, 4))
print(summa(3, 6))
print(summa(3, 9))
print("Функция вызывалась", summa.count, "раз")
