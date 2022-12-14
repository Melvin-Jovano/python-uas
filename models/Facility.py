from typing import Union
import uuid
from models.Product import RupiahToDollar, RupiahToYen

# Design Pattern: Observer => Publisher
class Facility:
  def __init__(self, name: str, locationId: str, productIds: 'list[str]' = [], id: Union[str, None] = None) -> None:
    from database import sales
    self._id = str(uuid.uuid4()) if id == None else id
    self.locationId = locationId
    self.name = name
    self.productIds = productIds

    # Register Subscriber
    self.subscriber = sales

  def showMenu(self, isRp, isYen, isDollar):
    from utilsFolder.text_style import TextStyle
    if len(self.productIds) == 0:
        print(f'{TextStyle.RED}No Products Were Found{TextStyle.END}')
    else:
        from database import product
        from database import productType

        menuHashmap = {}
        result = []

        for pt in productType:
            for facilityProduct in self.productIds:
                for p in product:
                    if facilityProduct == p._id and p.productTypeId == pt._id:
                        try:
                            result.append(p)
                            menuHashmap[pt.name].append(p)
                        except:
                            menuHashmap[pt.name] = [p]
        
        x = 1
        for a in menuHashmap:
            print(f'\n{TextStyle.BLUE}{a}:{TextStyle.END}')
            for p in menuHashmap[a]:
                if isRp:
                    print(f'{x}. {p.displayDescription()}')
                elif isDollar:
                    print(f'{x}. {RupiahToDollar(p).displayDescriptionInDollar()}')
                elif isYen:
                    print(f'{x}. {RupiahToYen(p).displayDescriptionInYen()}')
                x += 1

    return result
  
  def sellItem(self, amount, productId, customerId):
    # Notify Subscriber
    self.subscriber.addSale({
      'amount': amount,
      'productId': productId,
      'customerId': customerId,
    })