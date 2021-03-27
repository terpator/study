"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается
одинаково. Самое большое число-палиндром, полученное умножением двух
двузначных чисел: 9009 = 91 × 99. Найдите самый большой палиндром, полученный
умножением двух трехзначных чисел. Выведите значение этого палиндрома и то,
произведением каких чисел он является.
"""


def palin():
    palindrom = 0
    for x in range(100, 1000):
      for y in range(100, 1000):
        tmp = str(x * y)
        if tmp == tmp[::-1]:
          if int(tmp) > palindrom:
            palindrom = int(tmp)
            x_itog = x
            y_itog = y
            somelist = [palindrom, x_itog, y_itog]
    return somelist

somelist = palin()
print("Палиндром равен", somelist[0])
print("Множители: ", somelist[1], somelist[2])

        
            
    
