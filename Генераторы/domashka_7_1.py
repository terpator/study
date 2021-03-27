"""
Реализуйте генераторную функцию, которая будет возвращать по
одному члену геометрической прогрессии с указанным множителем.
Генератор должен остановить свою работу или по достижению указанной
границы, или при передаче команды на завершение.
"""


﻿def gen(start, stop, mnozh):
    i = start
    while i <=stop:
        try:
            yield i
        except:
            print("Exception")
            i = start
            return
        i *= mnozh
    return

g = gen(15, 10000, 2)
for i in g:
    print(i)
    if i == 3840:
        g.close()

print()

g = gen(15, 10000, 2)
for i in g:
    print(i)
    
    
