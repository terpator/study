"""
Дан треугольник координаты вершин которого А(0,0), В(4,4), С(6,1). Пользователь
вводит с клавиатуры координаты точки x и y. Написать программу, которая
определит, лежит ли эта точка внутри треугольника или нет.
"""


x = int(input("Введите координату Х: "))
y = int(input("Введите координату Y: "))
xA = 0
yA = 0
xB = 4
yB = 4
xC = 6
yC = 1
expr1 = (xA - x) * (yB - yA) - (xB - xA) * (yA - y)
expr2 = (xB - x) * (yC - yB) - (xC - xB) * (yB - y)
expr3 = (xC - x) * (yA - yC) - (xA - xC) * (yC - y)
if ((expr1 > 0) and (expr2 > 0) and (expr3 > 0)) or ((expr1 < 0) and (expr2 < 0) and (expr3 < 0)):
    print("Точка внутри треугольника")
else:
    print("Точка снаружи треугольника")





