class Category:
    """
    Класс категорий продукции
    """
    title: str
    description: str
    products: list

    def __init__(self, title, description, products):
        """
        Метод для инициализации экземпляра класса
        """
        self.title = title
        self.description = description
        self.products = products


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
        self.price = price
        self.in_stock = in_stock
