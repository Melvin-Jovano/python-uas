from models.Animal import Animal

class Arthropod(Animal):
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool, numberOfLegs : int, numberOfMolts : int, introTempate=None) -> None:
        super().__init__(scientificName, name, age, weight, habitatId, isEndangered, introTempate)
        self.numberOfLegs = numberOfLegs
        self.numberOfMolts = numberOfMolts