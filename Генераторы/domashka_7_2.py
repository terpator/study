"""
Реализуйте свой аналог генераторной функции range(). Да, вы теперь
знаете, что это - генератор.
"""


﻿def my_range(stop, start = 0, step = 1):
    i = start
    while i < stop:
        try:
            yield i
        except:
            print("Exception")
            i = start
            return
        i += step
    return

for i in my_range(20):
    print(i, end = " ")

print()

for i in my_range(start = 2, stop = 20):
    print(i, end = " ")
    
print()

for i in my_range(start = 2, stop = 20, step = 3):
    print(i, end = " ")

    
    
