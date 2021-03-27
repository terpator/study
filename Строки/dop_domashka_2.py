"""
Напишите программу для нахождения расстояние Левенштейна между двумя
строками.
Расстояние
Левенштейна
-
это
минимальное
количество
односимвольных изменений (вставки, удаления или замены), необходимых для
изменения одной строки в другую.
Пример:
"kitten" и "sitting". Расстояние равно 3.
Это перестановки вида kitten -> kittin -> sittin -> sitting
Подробнее тут: https://en.wikipedia.org/wiki/Levenshtein_distance
"""


a = input("Введите текст 1: ")
b = input("Введите текст 2: ")
n = len(a)
m = len(b)
if n > m:
     a, b = b, a
     n, m = m, n
current_row = range(n + 1)
for i in range(1, m + 1):
     previous_row = current_row
     current_row = [i] + [0] * n
     for j in range(1, n + 1):
          add = previous_row[j] + 1 
          delete = current_row[j - 1] + 1
          change = previous_row[j - 1]
          if a[j - 1] != b[i - 1]:
               change = change + 1
          current_row[j] = min(add, delete, change)
print("Расстояние Левенштейна равно ", current_row[n])
