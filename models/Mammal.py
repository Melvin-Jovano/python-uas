from models.Animal import Animal

class Mammal(Animal):
    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool,isNocturnal : bool, isCarnivore : bool, isHibernate : bool, introTempate=None) -> None:
        super().__init__(scientificName, name, age, weight, habitatId, isEndangered, introTempate)
        self.isNocturnal = isNocturnal
        self.isCarnivore = isCarnivore
        self.isHibernate = isHibernate