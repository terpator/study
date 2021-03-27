"""
Напишите программу, которая найдет самое длинное слово в текстовом
файле.
"""


def write_to_file(text, file_address = "input.txt"):
    f = open(file_address, "w")
    f.write(text)
    f.close()

def find_longest(file_address = "input.txt"):
    f = open(file_address, "r")
    text = f.read()
    f.close()
    text_list = text.split()
    longest = text_list[0]
    for word in text_list:
        if len(word) > len(longest):
            longest = word
    return longest

in_text = "English texts for beginners to practice reading and comprehension online and for free."
write_to_file(in_text, "input.txt")
print("Самое длинное слово: ", find_longest())
