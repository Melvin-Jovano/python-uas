from models.Product import Product

# Design Pattern: Decorator
class RupiahToDollar(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.000064
        self.product = product
    
    def displayDescriptionInDollar(self):
        if self.product.stock == 0:
            return f'{self.product.name}, ${self.ratio * self.product.price} | Out Of Stock'
        else:
            return f'{self.product.name}, ${self.ratio * self.product.price}'