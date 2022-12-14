from models.Animal import Animal

# Inheritance
class Reptiles(Animal):
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool, introTempate, hasShell: bool, numberOfEggs: int = 0) -> None:
        super().__init__(scientificName, name, age, weight, habitatId, isEndangered, introTempate)
        self.hasShell = hasShell
        self.numberOfEggs = numberOfEggs