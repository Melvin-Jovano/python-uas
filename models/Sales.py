from datetime import datetime

class Sales:
    def __init__(self, sales: list) -> None:
        self.sales = sales

    def addSale(self, sale):
        self.sales.append({
            'amount': sale['amount'],
            'productId': sale['productId'],
            'customerId': sale['customerId'],
            'date': datetime.now()
        })
        print('Item Sold Successfully')