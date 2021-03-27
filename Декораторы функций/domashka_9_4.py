"""
Создайте декоратор с параметрами для проведения хронометража работы
той или иной функции. Параметрами должны выступать то, сколько раз нужно
запустить декорируемую функцию и в какой файл сохранить результаты
хронометража. Цель - провести хронометраж декорируемой функции.
"""


﻿import time
import random

def dec(count, fname):
    def inner_func(f):
        def deep_inner(n):
            fin_res = f(n)
            start = time.time()
            i = 1
            while i <= count:
                f(n)
                i += 1 
            end = time.time()
            result = end - start
            stream = open(fname, "w")
            stream.write(str(result) + " секунд для " + str(count) + " вызовов")
            stream.close()
            return fin_res
        return deep_inner
    return inner_func

@dec(1000, "test.txt")
def list_comprehension(n):
    somelist = [random.randint(1, 1000) for x in range(n)]
    return somelist

list_comprehension(10)
print("Done! ")
