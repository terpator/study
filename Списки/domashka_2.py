"""
Создайте список случайных чисел (размером 4 элемента). Создайте второй список в два
раза больше первого, где первые 4 элемента должны быть равны элементам первого
списка, а остальные элементы заполните удвоенными значением начальных. Например,
Было → [1,4,7,2]
Стало → [1,4,7,2,2,8,14,4]
"""


import random
mylist = []
for i in range(4):
     mylist.append(random.randint(1, 20))
print(mylist)
list_add = []
for element in mylist:
       list_add.append(2 * element)
mylist = mylist + list_add
print(mylist)
     
