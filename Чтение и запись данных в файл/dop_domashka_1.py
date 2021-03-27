"""
Считайте из текстового файла текст на английском языке и выведите
статистику по частоте использования букв в тексте (т. е. буква — количество
использований).
Причем
первыми
должны
выводиться
буквы
используемые чаще всего.
"""


def stat(file_address = "input.txt"):
    f = open(file_address, "r")
    text = f.read()
    f.close()
    mydict= {}
    count = 0
    for char in text:
        if char.isalpha():
            count = mydict.get(char)
            if count:
                count = count + 1
            else:
                count  = 1
            mydict[char] = count
    return mydict

text = "!QQQQQQQQQQ ww!, 3444eeefkdfbgbkfgkfgnkfkfgpkfopkkffg"
print(text)
print()
f = open("input.txt", "w")
f.write(text)
f.close()

mydict = stat()
f = open("tmp.txt", "w")
list_of_values = sorted(mydict.values())
list_of_values = list_of_values[::-1]
for element in list_of_values:
    for dic_item in mydict:
        if mydict[dic_item] == element:
           tmpstr = dic_item + "-" + str(element)
           f.write(tmpstr + "\n")
f.close()

lines = []
f = open("tmp.txt", "r")
f_tmp = open("tmp2.txt", "w")
for line in f:
    if line not in lines:
        lines.append(line)
        f_tmp.write(line)
f_tmp.close()
f.close()

f = open("tmp2.txt", "r")
text = f.read()
print(text)
f.close()
