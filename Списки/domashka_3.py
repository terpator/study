"""
Создайте список из 12 элементов. Каждый элемент этого списка представляет собой
зарплату рабочего за месяц (случайное число от 7500 до 15000 грн.). Выведите этот
список на экран и вычислите среднемесячную зарплату этого рабочего.
"""


import random
mylist = []
for i in range(12):
     mylist.append(random.randint(7500, 15000))
print(mylist)
total = 0
for element in mylist:
     total = total + element
average = total / 12
print("Среднемесячная зарплата: ", int(average))

     
