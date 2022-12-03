import uuid

from models.Animal import Animal

class Habitat:
    def __init__(self, locationId: str, name: str) -> None:
        self._id = str(uuid.uuid4())
        self.locationId = locationId
        self.name = name

    def printIntro(self, animals: list[Animal]):
        print(f'There Are {len(animals)} Animal(s) Here, There Are:')

        n = 1
        for a in animals:
            print(f'{n}. {a.printInfo()}')
            n += 1