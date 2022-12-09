from models.Animal import Animal

class Amphibian(Animal):
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool, isPoisonous : bool, hasLegs : bool, numberOfLimbs : int, introTempate=None) -> None:
        super().__init__(scientificName, name, age, weight, habitatId, isEndangered, introTempate)
        self.isPoisonous = isPoisonous
        self.hasLegs = hasLegs
        self.numberOfLimbs = numberOfLimbs