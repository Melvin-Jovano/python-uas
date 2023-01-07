from typing import Union
import uuid
from utilsFolder.text_style import TextStyle

class Product:
    def __init__(self, name: str, price: int, stock: int, productTypeId: str, id: Union[str, None] = '') -> None:
        self._id = str(uuid.uuid4()) if id == None else id
        self.name = name
        self.price = price
        self.stock = stock
        self.productTypeId = productTypeId

    def displayDescription(self):
        if self.stock == 0:
            return f'{TextStyle.RED}{self.name}, Rp.{"{:20,.2f}".format(self.price).strip()} | Out Of Stock{TextStyle.END}'
        else:
            return f'{TextStyle.GREEN}{self.name}, Rp.{"{:20,.2f}".format(self.price).strip()}{TextStyle.END}'

class RupiahToDollar(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.000064
        self.product = product
    
    def displayDescriptionInDollar(self):
        if self.product.stock == 0:
            return f'{TextStyle.RED}{self.product.name}, ${self.ratio * self.product.price} | Out Of Stock{TextStyle.END}'
        else:
            return f'{TextStyle.GREEN}{self.product.name}, ${self.ratio * self.product.price}{TextStyle.END}'

class RupiahToYen(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.0088
        self.product = product
    
    def displayDescriptionInYen(self):
        if self.product.stock == 0:
            return f'{TextStyle.RED}{self.product.name}, ¥{self.ratio * self.product.price} | Out Of Stock{TextStyle.END}'
        else:
            return f'{TextStyle.GREEN}{self.product.name}, ¥{self.ratio * self.product.price}{TextStyle.END}'