from typing import Union
import uuid

class Product:
    def __init__(self, name: str, price: int, stock: int, productTypeId: str, id: Union[str, None] = '') -> None:
        self._id = str(uuid.uuid4()) if id == None else id
        self.name = name
        self.price = price
        self.stock = stock
        self.productTypeId = productTypeId

    def displayDescription(self):
        if self.stock == 0:
            return f'{self.name}, Rp.{"{:20,.2f}".format(self.price).strip()} | Out Of Stock'
        else:
            return f'{self.name}, Rp.{"{:20,.2f}".format(self.price).strip()}'

class RupiahToDollar(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.000064
        self.product = product
    
    def displayDescriptionInDollar(self):
        if self.product.stock == 0:
            return f'{self.product.name}, ${self.ratio * self.product.price} | Out Of Stock'
        else:
            return f'{self.product.name}, ${self.ratio * self.product.price}'

class RupiahToYen(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.0088
        self.product = product
    
    def displayDescriptionInYen(self):
        if self.product.stock == 0:
            return f'{self.product.name}, ¥{self.ratio * self.product.price} | Out Of Stock'
        else:
            return f'{self.product.name}, ¥{self.ratio * self.product.price}'