from datetime import datetime

class Sales:
    def __init__(self, sales: list) -> None:
        self.sales = sales

        totalSales = 0
        for s in self.sales:
            totalSales += s['amount']

        self.totalSales = totalSales
        self.yenRatio = 0.0088
        self.dollarRatio = 0.000064

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