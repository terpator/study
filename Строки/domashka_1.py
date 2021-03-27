"""
Напишите программу, которая посчитает сколько букв «b» в введенной строке
текста.
"""


text = input("Введите текст:")
text = text.lower()
count = 0
for char in text:
     if char == "b":
          count = count + 1
print("В данном тексте символ 'b' встречается " + str(count) + " раз(а)")
