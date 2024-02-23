from abc import ABC, abstractmethod


class AllProducts(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    class ForAllClassesMixin:
        def __repr__(self):
            return f'создан объект{self.__class__.__name__}'


class Product(AllProducts):
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
