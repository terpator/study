"""
Напишите функцию, которая вернет максимальное число из списка чисел.
"""


import random

def maxcalc(list_1):
    maxnumber = list_1[0]
    for num in list_1:
        if num > maxnumber:
            maxnumber = num
    return maxnumber

mylist = []
for i in range(10):
    mylist.append(random.randint(1, 100))
print(mylist)
print("Максимальное число в списке: ", maxcalc(mylist))
