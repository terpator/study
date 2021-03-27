"""
Напишите программу, которая вычитает текст из двух текстовых файлов.
Программа должна найти и записать в файл «result.txt» слова, которые есть
и в первом, и во втором файле одновременно. Например, если в первом
файле записано «Hello world», а во втором «Hello Java», то в
результирующем файле должно быть слово «Hello» так, как только это
слово есть и в первом и втором файле одновременно.
"""


def write_same_words(file_address_1, file_address_2):
    f_1 = open(file_address_1, "r")
    text_1 = f_1.read()
    text_1 = set(text_1.split())
    f_1.close()
    f_2 = open(file_address_2, "r")
    text_2 = f_2.read()
    text_2 = set(text_2.split())
    f_2.close()
    itog_list = list(text_1.intersection(text_2))
    f_result = open("result.txt", "w")
    for word in itog_list:
        f_result.write(word + "\n")
    f_result.close()

f_in1 = open("in1.txt", "w")
text1 = "Hello world not Java"
f_in1.write(text1)
f_in1.close()
f_in2 = open("in2.txt", "w")
text2 = "Hello everyone"
f_in2.write(text2)
f_in2.close()

write_same_words("in1.txt", "in2.txt")
f_result = open("result.txt", "r")
result_words = f_result.read()
f_result.close()
print(result_words)
