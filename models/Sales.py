from datetime import datetime

class Sales:
    def __init__(self, sales: list) -> None:
        self.sales = sales
        self.expense = []

        totalSales = 1_000_000
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

    def sell(self, amount, name):
        self.totalSales -= amount
        self.expense.append({
            'amount': amount,
            'name': name
        })

    def getTotalSales(self, isRp, isYen, isDollar):
        if not isRp:
            if isYen:
                return f'¥{"{:20,.2f}".format(self.yenRatio * self.totalSales).strip()}'
            elif isDollar:
                return f'${"{:0,.2f}".format(self.dollarRatio * self.totalSales).strip()}'
        return f'Rp.{"{:20,.2f}".format(self.totalSales).strip()}'