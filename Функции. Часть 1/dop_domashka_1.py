"""
Существуют такие последовательности чисел:
0,2,4,6,8,10,12
1,4,7,10,13
1,2,4,8,16,32
1,3,9,27
1,4,9,16,25
1,8,27,64,125
Реализуйте программу, которая выведет следующий член этой последовательности
(либо подобной им) на экран. Последовательность пользователь вводит с
клавиатуры в виде строки. Например, пользователь вводит строку 0,5,10,15,20,25 и
ответом программы должно быть число 30.
"""


def print_posled(text):
    somelist = text.split(",")
    if "0" in somelist:
        zakon_proizv = False
       
        diff = int(somelist[1]) - int(somelist[0])
        for i in range(len(somelist) - 1):
            if int(somelist[i + 1]) - int(somelist[i]) != diff:
                zakon_plus = False
                break
        else:
            zakon_plus = True
    else:
        mnozhitel = int(somelist[1]) / int(somelist[0])
        for i in range(len(somelist) - 1):
            if int(somelist[i + 1]) / int(somelist[i]) != mnozhitel:
                zakon_proizv = False
                break
        else:
            zakon_proizv = True

        diff = int(somelist[1]) - int(somelist[0])
        for i in range(len(somelist) - 1):
            if int(somelist[i + 1]) - int(somelist[i]) != diff:
                zakon_plus = False
                break
        else:
            zakon_plus = True

    if zakon_plus:
        return int(somelist[-1]) + diff
    elif zakon_proizv:
        return int(somelist[-1]) * mnozhitel
    else:
        return "Закономерность не обнаружена!"
       
text = input("Введите строку: ")
print(print_posled(text))
