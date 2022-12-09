from typing import Union
import uuid

class ProductType:
    def __init__(self, name: str, id: Union[str, None] = None) -> None:
        self._id = str(uuid.uuid4()) if id == None else id
        self.name = name