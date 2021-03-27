"""
Создайте консольный «текстовый редактор» с возможностью сохранения
набранного текста в файл. (Не переусердствуйте. Имеется в виду, что вы
сначала должны считать несколько строк с клавиатуры, а потом сохранить
считанный текст в файл).
"""


def write_to_file(file_address, text):
    f = open(file_address, "w")
    text = "\n".join(text)
    f.write(text)
    f.close()

text = []
print("Введите текст для сохранения в файле 'input.txt'. Для признака конца - введите пустую строку: ")
while True:
    textline = input()
    text.append(textline)
    if textline == "":
        break
write_to_file("input.txt", text)




