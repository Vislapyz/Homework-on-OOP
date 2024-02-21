class Category:
    """
    Класс категорий продукции
    """
    title: str
    description: str
    __products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self,
                 title: str,
                 description: str,
                 products: list):
        """
        Метод для инициализации экземпляра класса
        """
        self.title = title
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def __str__(self):
        """
        Класс Category возрощает строковое представление
        """
        return f'{self.title}, количество продуктов {len(self)} шт.'

    def __len__(self):
        """
        Общее количество всех товаров
        """
        all_product = 0
        for product in self.all_products():
            all_product += int(product.in_stock)
        return all_product

    def adding_products(self, product):
        """
        Mетод принимает на вход объект товара и добавлять его в список
        """
        if issubclass(product.__class__, Product):
            self.__products.append(product)
            return self.__products
        raise TypeError('Добавить только продукт')

    @property
    def get_list_product(self):
        """
        Геттер, который выводить список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт.
        """
        list_product = []
        for product in self.__products:
            list_product.append(f'{product.title}, {product.price} руб. Остаток: {product.in_stock} шт.')
        return list_product

    def all_products(self):
        """Для всех продуктов в списке класс Category
        """
        return self.__products


class Product:
    """
    Класс продукций и количества
    """
    title: str
    description: str
    price: float
    in_stock: int
    color: str

    def __init__(self,
                 title: str,
                 description: str,
                 price: float,
                 in_stock: int,
                 color_c: str):
        """
        Метод для инициализации экземпляра класса
        """
        self.title = title
        self.description = description
        self.__price = price
        self.in_stock = in_stock
        self.color_c = color_c

    def __str__(self):
        """
        Для класса Product добавить строковое отображение
        """
        return f'{self.title},{self.price} руб. Остаток: {self.in_stock}'

    def __add__(self, other):
        """
        Складывать товары одного класса продукты
        """
        if type(self) == type(other):
            return self.price * self.in_stock + other.price * other.in_stock
        raise TypeError('Ошибка типа класса')

    @classmethod
    def creates_product(cls, title, description, price, in_stock, color_c):
        """
        Cоздает товар и возвращает объект, который можно добавлять в список товаров.
        """
        return cls(title, description, price, in_stock, color_c)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('цена введена некорректная')
        else:
            self.__price = new_price


class SmartPhones(Product):
    """
    Класс смартфон наследние от класса Product
    """
    efficiency: float
    model: str
    internal_memory: str

    def __init__(self,
                 title: str,
                 description: str,
                 price: float,
                 in_stock: int,
                 color_c: str,
                 efficiency: float,
                 model: str,
                 internal_memory: str):
        super().__init__(title, description, price, in_stock, color_c)
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory


class LawnGrass(Product):
    """
    Класс трава газонная наследние от класса Product
    """
    production: str
    germination: str

    def __init__(self,
                 title: str,
                 description: str,
                 price: float,
                 in_stock: int,
                 color_c: str,
                 production: str,
                 germination: str):
        super().__init__(title, description, price, in_stock, color_c)
        self.production = production
        self.germination = germination
