"""
Напишите программу которая считает строку текста с клавиатуры и выведет на
экран статистику, сколько раз какая буква встречается в этой строке. Например,
для строки «Hello world» эта статистика выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д.
"""


text = input("Введите строку: ")
mydict = {}
for char in text:
     count = mydict.get(char)
     if count:
          count = count + 1
     else:
          count = 1
     mydict[char] = count

for key in mydict.keys():
     print(key, "->", mydict[key], "раз")
     
     
