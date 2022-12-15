from typing import Union
import uuid

class Facility:
      def __init__(self, locationId: str, name: str, productIds: 'list[str]' = [], id: Union[str, None] = None) -> None:
        self._id = str(uuid.uuid4()) if id == None else id
        self.locationId = locationId
        self.name = name
        self.productIds = productIds

      def showMenu(self):
        pass

      def insertProduct(self):
        pass