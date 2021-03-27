"""
Напишите функцию-генератор, которая будет возвращать простые числа.
Верхняя граница этого диапазона должна быть задана параметром этой
функции.
"""


﻿def isprime(n):
    if n <= 3:  
        return True
    elif n % 2 == 0: 
        return False
    else:
        for i in range(3, n, 2):
            if i * i > n:
               break
            if n % i == 0:
               return False
    return True

def gen_simple(limit):
    for i in range(2, limit):
        try:
            if isprime(i):
                yield i
        except:
            print("Exception")
            return
    return

for i in gen_simple(100):
    print(i, end = " ")
 
