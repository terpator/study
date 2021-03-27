"""
Напишите программу, которая вычитает текст из текстового файла и
выведет на экран, сколько раз в тексте встречается буква «A».
"""


def count_symbol(file_address,symbol):
    f = open(file_address, "r")
    text = f.read()
    f.close()
    count = 0
    for char in text:
        if char == symbol:
            count = count + 1
    return count

text = "Amy normally hated Monday mornings, but this year was different."
file_example = open("input.txt", "w")
file_example.write(text)
file_example.close()
symbol = "A"
count = count_symbol("input.txt", symbol)
print(text)
print("Количество символов {letter} равно".format(letter = symbol), count)
