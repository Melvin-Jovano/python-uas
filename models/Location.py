from typing import Union
import uuid

class Location:
    def __init__(self, name: str, description: bool, id: Union[str, None] = None) -> None:
        self._id = str(uuid.uuid4()) if id == None else id
        self.name = name
        self.description = description