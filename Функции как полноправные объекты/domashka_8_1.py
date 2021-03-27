"""
Реализуйте генераторную функцию, которая будет возвращать по одному
члену числовой последовательности, закон которой задается с помощью
пользовательской функции. Кроме этого параметром генераторной функции
должны быть значение первого члена прогрессии и количество выдаваемых
членов последовательности (n). Генератор должен остановить свою работу
или по достижению n — го члена , или при передаче команды на завершение.
"""


﻿def gen(zakon, start, n):
    i = start
    counter = 1
    while counter <= n:
        try:
            yield str(i) + " - " + str(zakon(i))
        except:
            print("Exception")
            i = start
            return
        counter += 1
        i += 1
    return

def user_zakon(number):
    return number ** 2

print("Закон - квадраты чисел")
print()
g = gen(user_zakon, 1, 10)
for i in g:
    print(i)
    if i == "4 - 16":
        g.close()

print()

g = gen(user_zakon, 1, 10)
for i in g:
    print(i)
    
