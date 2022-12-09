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
            return f'{self.name}, Rp.{self.price} | Out Of Stock'
        else:
            return f'{self.name}, Rp.{self.price}'
