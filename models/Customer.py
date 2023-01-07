from typing import Union
import uuid
from models.enums.Gender import Gender

class Customer:
    def __init__(self, name: str, age: int, gender: Gender,  id: 'Union[str, None]' = None) -> None:
        self._id = str(uuid.uuid4()) if id == None else id
        self.name = name
        self.age = age
        self.gender = gender
        self.isCheckOut = False