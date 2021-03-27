"""
Напишите программу, которая запишет в файл список целых чисел.
"""


def write_to_file(somelist, file_address):
    f = open(file_address, "w")
    for element in somelist: 
        f.write(str(element) + "," + "\n")
    f.close()

somelist = [5, 6, 1, 2, 8, 1, 9, 4]
write_to_file(somelist, "result.csv")

    
