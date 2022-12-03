import uuid
from models.Animal import Animal

class Habitat:
    def __init__(self, locationId: str, name: str) -> None:
        self._id = str(uuid.uuid4())
        self.locationId = locationId
        self.name = name

    def printIntro(self):
        from database import animal
        
        animals: list[Animal] = []

        for a in animal:
            if a.habitatId == self._id:
                animals.append(a)

        if len(animals) == 0:
            print('No Animals Were Found')
        else:
            print(f'There Are {len(animals)} Animal(s) Here, There Are:')

            n = 1
            for a in animals:
                if a.habitatId == self._id:
                    print(f'{n}. {a.printInfo()}')
                    n += 1