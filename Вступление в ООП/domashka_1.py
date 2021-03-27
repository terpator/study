"""
Создайте пользовательский класс для описания товара (предположим,
это задел для интернет-магазина). В качестве полей товара можете
использовать значение цены, описание, габариты товара. Создайте пару
экземпляров вашего класса и протестируйте их работу.

Создайте класс «Покупатель». В качестве полей можете использовать
фамилию, имя, отчество, мобильный телефон и т. д.

Создайте класс «Заказ». Заказ может содержать несколько товаров.
Заказ должен содержать данные о пользователе, который его осуществил.
Реализуйте метод вычисления суммарной стоимости заказа. Определите
метод __str__() для корректного вывода информации о этом заказе.
"""


class Product:
    def __init__(self, price, desription, length, width, hight):
        self.price = price
        self.description = desription
        self.length = length
        self.width = width
        self.hight = hight
    
    def __str__(self):
        return "Product [price = {}, description = {}, length = {}, width = {}, hight = {}]".format(
            self.price,self.description,self.length,self.width,self.hight)

class Buyer:
    def __init__(self, lastname, firstname, patronymic, mobile):
        self.lastname = lastname
        self.firstname = firstname
        self.patronymic = patronymic
        self.mobile = mobile
    
    def __str__(self):
        return "Buyer [lastname = {}, firstname = {}, patronymic = {}, mobile = {}]".format(
            self.lastname,self.firstname,self.patronymic,self.mobile)

class Order:
    def __init__(self):
        self.order_list = {}
    
    def __str__(self):
        result_product = ""
        for k, v in self.order_list.items():
            result_product += str(k)+"\n"+"Количество: "+str(v)+"\n"
        return f"Покупатель: {self.buyer.lastname} {self.buyer.firstname} {self.buyer.patronymic}" + \
        "\n" + f"(Телефон): {self.buyer.mobile}" + "\n" + result_product
    
    def add_product(self, product, amount):
        self.order_list[product] = amount
    
    def init_buyer(self, buyer):
        self.buyer = buyer
    
    def count_cost(self):
        self.cost = 0
        for k, v in self.order_list.items():
            self.cost += k.price * v



product_1 = Product(100,"Yellow box",10,10,10)
product_2 = Product(200,"White box",20,10,30)
print("Продукт 1:")
print(product_1)
print()
print("Продукт 2:")
print(product_2)
print()
buyer_1 = Buyer("Иванов", "Иван", "Иванович", "+380961112233")
print("Покупатель:")
print(buyer_1)
print()
order_1 = Order()
order_1.init_buyer(buyer_1)
order_1.add_product(product_1, 5)
order_1.add_product(product_2, 3)
order_1.count_cost()
print("Заказ:")
print(order_1)
print("Итого к оплате: ", order_1.cost)
