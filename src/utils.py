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
        self.title = title
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_unique_products += 1

    def adding_products(self, product):
        self.__products.append(product)


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
