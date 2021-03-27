"""
Реализуйте функцию рисующую на экране прямоугольник из звездочек «*». Ее
параметрами будут целые числа, которые описывают длину и ширину такого
прямоугольника.
"""


def print_triangle(h,w):
    i = 1
    while i <= h:
        j = 1
        while j <= w:
            if i==1 or i==h or j==1 or j==w:
                print("*", end = "")
            else:
                print(" ", end = "")
            j = j + 1
        print()
        i = i + 1

h = int(input("Введите высоту: "))
w = int(input("Введите ширину: "))
print_triangle(h,w)
