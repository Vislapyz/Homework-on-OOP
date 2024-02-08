class Category:
    """
    Класс категорий продукции
    """
    title: str
    description: str
    products: list

class Product:
    """
    Класс продукций и количества
    """
    title: str
    description: str
    price: int
    in_stock: int