import uuid
from models.Animalia import Animalia
from utils.info_template import defaultIntro

class Animal(Animalia):
    scientificName: str = ''
    name: str = ''
    age: int = 0
    weight: int= 0
    habitatId: str = 0
    isEndangered: bool = False

    def __init__(self, scientificName: str, name: str, age: int, weight: int, habitatId: str, isEndangered: bool, introTempate = None) -> None:
        super(Animalia, self).__init__()
        self._id = str(uuid.uuid4())
        self.scientificName = scientificName
        self.name = name
        self.age = age
        self.weight = weight
        self.habitatId = habitatId
        self.isEndangered = isEndangered
        
        print(123, introTempate)

        if introTempate == None:
            self.introTemplate = defaultIntro(self)
        else:
            self.introTemplate = introTempate(self)

    def printInfo(self) -> str:
        return self.introTemplate
    
    def __repr__(self):
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())