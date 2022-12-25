from typing import Union
import uuid

class Facility:
  def __init__(self, name: str, locationId: str, productIds: 'list[str]' = [], id: Union[str, None] = None) -> None:
    self._id = str(uuid.uuid4()) if id == None else id
    self.locationId = locationId
    self.name = name
    self.productIds = productIds

  def showMenu(self):
    if len(self.productIds) == 0:
      print('No Products Were Found')
    else:
      from database import product
      n = 1
      for facilityProduct in self.productIds:
        for p in product:
          if facilityProduct == p._id:
            print(f'{n}. {p.displayDescription()}')
            n += 1