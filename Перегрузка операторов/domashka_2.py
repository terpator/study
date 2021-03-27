"""
Создайте класс «Правильная дробь» и реализуйте методы сравнения,
сложения, вычитания и произведения для экземпляров этого класса.
"""


class ProperFraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.res = self.numerator / self.denominator

    def __eq__(self, other):
        return self.res == other.res

    def __gt__(self, other):
        return self.res > other.res

    def nod(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n
            
    def __add__(self, other):
        newnum = self.numerator * other.denominator + self.denominator * other.numerator
        newdenom = self.denominator * other.denominator
        common = self.nod(newnum, newdenom)
        return ProperFraction(newnum // common, newdenom // common)

    def __sub__(self, other):
        newnum = self.numerator * other.denominator - self.denominator * other.numerator
        newdenom = self.denominator * other.denominator
        common = self.nod(newnum, newdenom)
        return ProperFraction(newnum // common, newdenom // common)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __mul__(self, other):
        newnum = self.numerator * other.numerator
        newdenom = self.denominator * other.denominator
        common = self.nod(newnum, newdenom)
        return ProperFraction(newnum // common, newdenom // common)

frac_1 = ProperFraction(2, 5)
frac_2 = ProperFraction(1, 3)
print("{}/{} < {}/{}".format(frac_1.numerator,frac_1.denominator,frac_2.numerator,frac_2.denominator))
print(frac_1.numerator/frac_1.denominator < frac_2.numerator/frac_2.denominator)
print()
print("{}/{} == {}/{}".format(frac_1.numerator,frac_1.denominator,frac_2.numerator,frac_2.denominator))
print(frac_1.numerator/frac_1.denominator == frac_2.numerator/frac_2.denominator)
print()
frac_3 = frac_1 + frac_2
print("Сумма дробей", frac_3)
print()
frac_3 = frac_1 - frac_2
print("Разность дробей", frac_3)
print()
frac_3 = frac_1 * frac_2
print("Произведение дробей", frac_3)
