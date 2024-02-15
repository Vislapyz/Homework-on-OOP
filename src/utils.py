class Category:
    """
    Класс категорий продукции
    """
    title: str
    description: str
    __products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, title, description, products):
        """
        Метод для инициализации экземпляра класса
        """
        self.products = None
        self.title = title
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_unique_products += 1

    def adding_products(self, product):
        """
        Mетод принимает на вход объект товара и добавлять его в список
        """
        self.__products.append(product)

    @property
    def get_list_product(self):
        """
        Геттер, который выводить список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт.
        """
        list_product = []
        for product in self.__products:
            list_product.append( f'{product.title}, {product.price} руб. Остаток: {product.in_stock} шт.')
        return list_product

class Product:
    """
    Класс продукций и количества
    """
    title: str
    description: str
    price: float
    in_stock: int

    def __init__(self, title, description, price, in_stock):
        """
        Метод для инициализации экземпляра класса
        """
        self.title = title
        self.description = description
        self.__price = price
        self.in_stock = in_stock

    @classmethod
    def creates_product(cls, title, description, price, in_stock):
        """
        Cоздает товар и возвращает объект, который можно добавлять в список товаров.
        """
        return cls(title, description, price, in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def new_price(self, new_price):
        if new_price <= 0:
            print('цена введена некорректная')
        else:
            self.__price = new_price



