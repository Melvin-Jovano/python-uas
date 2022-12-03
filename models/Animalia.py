import abc

class Animalia(metaclass=abc.ABCMeta):
    @property 
    @abc.abstractproperty
    def scientificName(self):
        pass
    
    def name(self):
        pass

    def age(self):
        pass

    def weight(self):
        pass

    def habitatId(self):
        pass
    
    def isEndangered(self):
        pass

    @abc.abstractclassmethod
    def printInfo(self):
        pass