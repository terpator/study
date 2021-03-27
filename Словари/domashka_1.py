"""
Используя словарь, напишите программу, которая выведет на экран название дня
недели по его номеру. (1 - «Monday»)
"""


day = int(input("Введите номер дня недели (1-Monday...7-Sunday): "))
if day < 1 or day > 7:
     print("Введен некорректный номер!")
else:
     week = {
          1: "Monday",
          2: "Tuesday",
          3: "Wednesday",
          4: "Thursday",
          5: "Friday",
          6: "Saturday",
          7: "Sunday"
     }
     print(week[day])
