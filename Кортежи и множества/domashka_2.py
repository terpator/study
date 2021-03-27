"""
Напишите программу, которая сгенерирует два списка. Один с числами кратными
3, другой с числами кратными 5. С помощью множеств создайте список с числами,
которые есть в обоих множествах.
"""


list_3 = []
list_5 = []
for i in range(1,50):
    if i % 3 == 0:
        list_3.append(i)
    if i % 5 == 0:
        list_5.append(i)
print("Список чисел, кратных 3:")
print(list_3)
print("Список чисел, кратных 5:")
print(list_5)
set_3 = set(list_3)
set_5 = set(list_5)
itog = set_3.intersection(set_5)
itog_list = list(itog)
itog_list.sort()
print("Общие числа для обоих списков:")
print(itog_list)
