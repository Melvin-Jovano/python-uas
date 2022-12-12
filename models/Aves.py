from models.Animal import Animal

class Aves(Animal):
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, wingspan : int, canFly: bool, isEndangered: bool, introTempate=None) -> None:
        super().__init__(scientificName, name, age, weight, habitatId, isEndangered, introTempate)
        self.canFly = canFly
        self.wingspan = wingspan