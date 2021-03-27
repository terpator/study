"""
Напишите функцию, которая реализует линейный поиск элемента в списке целых
чисел. Если такой элемент в списке есть, то верните его индекс, если нет, то
верните число «-1».
"""


import random

def findnum(somelist, n):
    numindex = -1
    for element in somelist:
        if element == n:
            numindex = somelist.index(n)
    return numindex

somelist = []
for i in range(10):
    somelist.append(random.randint(1,100))
print(somelist)
n = int(input("Введите число для поиска: "))
numindex = findnum(somelist, n)
if numindex != -1:
    print("Число находится на позиции {num} индекса".format(num = numindex))
else:
    print("Такого числа в списке нет! {num}".format(num = numindex))
            
