"""
Напишите программу, которая реализует функциональность считывания
с клавиатуры стоимости товара. При этом стоит учесть, что пользователь
может ввести не цифры, а смесь цифр и букв или отрицательное число. При
необходимости создайте пользовательское исключение и обработайте его
(например, для отрицательных чисел).
"""


class NegativeOrZeroSumError(Exception):

    def __init__(self):
        super().__init__()
        self.message = "Введите сумму больше 0"

    def __str__(self):
        return self.message

while True:
    try:
        sum = int(input("Введите стоимость товара: "))
        if sum <= 0:
            raise NegativeOrZeroSumError            
    except ValueError:
        print("Введите только цифры")
    except NegativeOrZeroSumError as err:
        print(err)
    else:
        print(f"Стоимость товара: {sum}")
        break
