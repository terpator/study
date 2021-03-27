"""
Представьте описание кота (домашнее животное) на основе словаря.
"""


import random
names = ["Vaska", "Markiz", "Barsik"]
colors = ["Grey", "Black", "White"]
poroda_s = ["Персидская", "Сиамская", "Сфинкс"]
cats = []
for i in range(3):
     cat = {
          "name": names[i],
          "age": random.randint(1, 15),
          "color": colors[i],
          "weight": random.randint(1,10),
          "poroda": poroda_s[i]
     }
     cats.append(cat)
for j in range(3):
     print(cats[j])
