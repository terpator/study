"""
Используя функцию замыкания реализуйте такой прием программирования
как Мемоизация - https://en.wikipedia.org/wiki/Memoization
Используйте полученный механизм для ускорения функции рекурсивного
вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
просто рекурсивным подходом.
"""


﻿import time

def fibonacci_mem(n):
    cache = {0:0,1:1}
    def fib(n):
        if n in cache:
            return cache[n]
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib

def fibonacci(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print()
print("Мемоизация в действии (n=30)")
print()
start = time.time()
f=fibonacci_mem(30) 
for i in range(30):
    print(f(i), end = " ")
end = time.time()
print()
print("Заняла: ", end - start, "секунд")
print()
print()
print("Обычная рекурсия (n=30)")
print()
start = time.time()
for i in range(30):
    print(fibonacci(i), end = " ")
end = time.time()
print()
print("Заняла: ", end - start, "секунд")
