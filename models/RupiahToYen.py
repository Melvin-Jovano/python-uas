from models.Product import Product

# Design Pattern: Decorator
class RupiahToYen(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.0088
        self.product = product
    
    def displayDescriptionInYen(self):
        if self.product.stock == 0:
            return f'{self.product.name}, ¥{self.ratio * self.product.price} | Out Of Stock'
        else:
            return f'{self.product.name}, ¥{self.ratio * self.product.price}'