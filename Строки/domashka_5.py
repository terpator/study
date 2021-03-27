"""
Вводится строка из слов, разделенных пробелами. Найти самое длинное слово и
вывести его на экран.
"""


text = input("Введите текст: ")
mylist = text.split()
longest = mylist[0]
for elem in mylist:
     if len(elem) > len(longest):
          longest = elem
print("Самое длинное слово: ", longest)
