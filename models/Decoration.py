from typing import Union
import uuid

class Decoration:
  def __init__(self, name: str, locationId: str, id: Union[str, None] = None) -> None:
    self._id = str(uuid.uuid4()) if id == None else id
    self.locationId = locationId
    self.name = name