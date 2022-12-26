from typing import Union
import uuid
from models.RupiahToDollar import RupiahToDollar
from models.RupiahToYen import RupiahToYen
from models.Sales import Sales

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
    if len(self.productIds) == 0:
      print('No Products Were Found')
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
        print(f'\n{a}:')
        for p in menuHashmap[a]:
          if isRp:
            print(f'{x}. {p.displayDescription()}')
          elif isDollar:
            print(RupiahToDollar(p).displayDescriptionInDollar())
          elif isYen:
            print(RupiahToYen(p).displayDescriptionInYen())
          x += 1

      return result
  
  def sellItem(self, amount, productId, customerId):
    # Notify Subscriber
    self.subscriber.addSale({
      'amount': amount,
      'productId': productId,
      'customerId': customerId,
    })