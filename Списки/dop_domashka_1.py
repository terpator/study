"""
«Перевернуть матрицу». Т.е. написать программу, которая повернет базовую
матрицу на 90,180,270 градусов по часовой стрелке. (При выполнении задания
использовать дополнительную матрицу нельзя).
"""


import random
mylist = []
for i in range(6):
     row = []
     for j in range(6):
          row.append(random.randint(1,9))
     mylist.append(row)

for element in mylist:
     print(element)

n = 6
print()
print("Поворот на 90 градусов:")
i = 0
while i < n:
    j = i + 1  
    while j < n:  
       temp = mylist[i][j]
       mylist[i][j] = mylist[j][i]
       mylist[j][i] = temp
       j = j + 1 
    i = i + 1
i = 0
while i < n:
    j = 0  
    while j < n / 2: 
       temp = mylist[i][n - j - 1]
       mylist[i][n - j - 1] = mylist[i][j]
       mylist[i][j] = temp
       j = j + 1
    i = i + 1  
for element in mylist:
    print(element)
print()
print("Поворот на 180 градусов:")
i = 0
while i < n:
    j = i + 1  
    while j < n:  
       temp = mylist[i][j]
       mylist[i][j] = mylist[j][i]
       mylist[j][i] = temp
       j = j + 1 
    i = i + 1
i = 0
while i < n:
    j = 0  
    while j < n / 2: 
       temp = mylist[i][n - j - 1]
       mylist[i][n - j - 1] = mylist[i][j]
       mylist[i][j] = temp
       j = j + 1
    i = i + 1
for element in mylist:
    print(element)
print()
print("Поворот на 270 градусов:")
i = 0
while i < n:
    j = i + 1  
    while j < n:  
       temp = mylist[i][j]
       mylist[i][j] = mylist[j][i]
       mylist[j][i] = temp
       j = j + 1 
    i = i + 1
i = 0
while i < n:
    j = 0  
    while j < n / 2: 
       temp = mylist[i][n - j - 1]
       mylist[i][n - j - 1] = mylist[i][j]
       mylist[i][j] = temp
       j = j + 1
    i = i + 1
for element in mylist:
    print(element)
