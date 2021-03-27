"""
Напишите функцию, которая вернет сумму всех нечетных элементов списка.
Например, для списка вида [2,1,4,6,3] ваша программа должна вернуть 4.
"""


def summa_nech(somelist):
    summa = 0
    for element in somelist:
        if element % 2 != 0:
            summa = summa + element
    return summa

somelist = [2, 1, 4, 6, 3]
print(somelist)
print("Сумма нечетных элементов списка равна", summa_nech(somelist))
