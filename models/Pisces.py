from models.Animal import Animal
from enum import Enum, EnumMeta

class Pisces(Animal):
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool, length: int, group, introTempate=None) -> None:
        super().__init__(scientificName, name, age, weight, habitatId, isEndangered, introTempate)
        self.length = length
        self.group = group

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True
    
class BaseEnum(Enum, metaclass = MetaEnum):
    pass

class PiscesGroup(BaseEnum):
    BONY = "BONY"
    CATILAGIOUS = "CATILAGIOUS"
    LAMPREY = "LAMPREY"

