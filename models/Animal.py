import uuid
from models.Animalia import Animalia

class Animal(Animalia):
    scientificName: str = ''
    name: str = ''
    age: int = 0
    weight: int= 0
    habitatId: str = 0
    isEndangered: bool = False

    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool) -> None:
        super(Animalia, self).__init__()
        self._id = str(uuid.uuid4())
        self.scientificName = scientificName
        self.name = name
        self.age = age
        self.weight = weight
        self.habitatId = habitatId
        self.isEndangered = isEndangered

    def printInfo() -> str:
        return 'Hello There'