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