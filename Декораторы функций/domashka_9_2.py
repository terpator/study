"""
Создайте декоратор, который зарегистрирует декорируемую функцию в
списке функций, для обработки последовательности.
"""


﻿my_function = []

def add_function(f):
    my_function.append(f)
    return f

@add_function
def sum_elem(somelist):
    result = 0
    for element in somelist:
        result += element
    return result

@add_function
def mnozh_elem(somelist):
    result = 0
    for element in somelist:
        result *= element
    return result

print(my_function)
