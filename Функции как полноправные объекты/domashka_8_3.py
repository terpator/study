"""
Напишите функцию, которая применит к списку чисел произвольную
пользовательскую функцию и вернет суммы элементов полученного списка.
"""


﻿def func(seq, zakon):
    tmp_list = []
    for element in seq:
        tmp_list.append(zakon(element))
    sum = 0
    for element in tmp_list:
        sum += element
    return sum

def user_func(n):
    return n ** 2

my_list = [5, 5, 7, 2, 7, 8]
result = func(my_list, user_func)
print(result)
    
