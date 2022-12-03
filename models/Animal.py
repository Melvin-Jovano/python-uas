import uuid

class Animal:
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: int, isEndangered: bool) -> None:
        self._id = str(uuid.uuid4())
        self.scientificName = scientificName
        self.name = name
        self.age = age
        self.weight = weight
        self.habitatId = habitatId
        self.isEndangered = isEndangered

    @property
    def getId(self):
        return self._id