from typing import Union
from models.Amphibian import Amphibian
from models.Arthropod import Arthropod
from models.Aves import Aves
from models.Customer import Customer
from models.Facility import Facility
from models.Habitat import Habitat
from models.Location import Location
from models.Mammal import Mammal
from models.Pisces import Pisces
from models.Sales import Sales
from models.Shop import Shop
from models.Staff import Staff
from models.Product import Product
from models.ProductType import ProductType
from models.Reptiles import Reptiles
from models.Decoration import Decoration

animal: list[Union[Aves, Amphibian, Arthropod, Mammal, Pisces, Reptiles]] = []
customer: list[Customer] = []
facility: list[Facility] = []
habitat: list[Habitat] = []
sales: list[Sales] = []
shop: list[Shop] = []
staff: list[Staff] = []
product: list[Product] = []
productType: list[ProductType] = []
decoration: list[Decoration] = []

location: list[Location] = [
    Location('BLOCK A', 'This Is The Insects Section'),
    Location('BLOCK B', 'U Can See All Kind Of Fishes Here'),
    Location('BLOCK C', 'Birds Fly Freely In This Place'),
    Location('BLOCK D', 'This Is Where The Reptile Habitats'),
    Location('BLOCK E', 'Pandas, Zebras And Other Mammals Live Here'),
    Location('BLOCK F', 'Amphibians Dominated This Location'),
    Location('Park', 'Food Or Drink Stands Goes Here')
]