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

animal: 'list[Union[Aves, Amphibian, Arthropod, Mammal, Pisces, Reptiles]]' = []
customer: 'list[Customer]' = []
facility: 'list[Facility]' = []
habitat: 'list[Habitat]' = []
sales: 'list[Sales]' = []
shop: 'list[Shop]' = []
staff: 'list[Staff]' = []
decoration: 'list[Decoration]' = []

location: 'list[Location]' = [
    Location('BLOCK A', 'This Is The Insects Section', 'block-a'),
    Location('BLOCK B', 'U Can See All Kind Of Fishes Here', 'block-b'),
    Location('BLOCK C', 'Birds Fly Freely In This Place', 'block-c'),
    Location('BLOCK D', 'This Is Where The Reptile Habitats', 'block-d'),
    Location('BLOCK E', 'Pandas, Zebras And Other Mammals Live Here', 'block-e'),
    Location('BLOCK F', 'Amphibians Dominated This Location' 'block-f'),
    Location('Park', 'Food Or Drink Stands Goes Here', 'park')
]

productType: 'list[ProductType]' = [
    ProductType('Animal Food', 'animal-food'),
    ProductType('Soda', 'soda'),
    ProductType('Cold Drink', 'cold-drink'),
    ProductType('Frozen Food', 'frozen-food'),
    ProductType('Snack', 'snack'),
    ProductType('Meal', 'meal'),
    ProductType('Accessory', 'accessory'),
    ProductType('Ticket', 'ticket')
]

product: 'list[Product]' = [
    Product('Coca Cola', 8000, 60, 'soda', '6b59f7eb-0b81-45a7-beeb-23b55c336386'),
    Product('NESCAFÉ', 8000, 100, 'cold-drink', '034fad5f-3e56-44fd-b158-338de4af43d7'),
    Product('Dr. Pepper', 8000, 80, 'soda', '3237c7eb-f8b3-4945-bffe-07946db930dd'),
]