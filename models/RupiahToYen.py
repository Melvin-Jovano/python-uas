from models.Product import Product

# Design Pattern: Decorator
class RupiahToYen(Product):
    def __init__(self, product: Product) -> None:
        self.ratio = 0.0088
        self.product = product
    
    def convert(self):
        return self.ratio * self.product.price