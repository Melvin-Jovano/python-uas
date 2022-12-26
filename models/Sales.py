from datetime import datetime

class Sales:
    def __init__(self, sales: list) -> None:
        self.sales = sales
        self.totalSales = 0
        self.yenRatio = 0.0088
        self.dollarRatio = 0.000064
        # return f'${self.ratio * self.product.price}'

    def addSale(self, sale):
        self.sales.append({
            'amount': sale['amount'],
            'productId': sale['productId'],
            'customerId': sale['customerId'],
            'date': datetime.now()
        })
        self.totalSales += sale['amount']
        print('Item Sold Successfully')

    def getTotalSales(self, isRp, isYen, isDollar):
        if not isRp:
            if isYen:
                return f'¥{self.yenRatio * self.totalSales}'
            elif isDollar:
                return f'${self.dollarRatio * self.totalSales}'
        return f'Rp.{"{:20,.2f}".format(self.totalSales).strip()}'