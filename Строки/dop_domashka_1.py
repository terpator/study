"""
Вовочка сидя на уроке писал подряд одинаковые слова (слово может состоять из
одной буквы). Когда Марья Ивановна забрала у него тетрадь, там была одна строка
текста. Напишите программу, которая определит самое короткое слово из
написанных Вовочка. Например:
aaaaaaa — Вовочка писал слово - «a»
ititititit — Вовочка писал слово - «it»
catcatcatcat — Вовочка писал слово - «cat»
"""


text = input("Введите текст: ")
mylist = text.split()
list_shablonov = []
for word in mylist:
     tmpstr = ""
     for char in word:
          if char not in tmpstr:
               tmpstr = tmpstr + char
     list_shablonov.append(tmpstr)

shortest = list_shablonov[0]
for elem in list_shablonov:
     if len(elem) < len(shortest):
          shortest = elem
print("Самое короткое слово: ", shortest)
                    
