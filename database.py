from models.Animal import Animal
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

animal: list[Animal] = []
aves: list[Aves] = []
amphibian: list[Amphibian] = []
customer: list[Customer] = []
arthropod: list[Arthropod] = []
facility: list[Facility] = []
habitat: list[Habitat] = []
location: list[Location] = [
    Location('BLOCK A', 'This Is Where Arthropod Habitats'), 
    Location('Park', 'Food / Drink Stands Goes Here')
]
mammal: list[Mammal] = []
pisces: list[Pisces] = []
sales: list[Sales] = []
shop: list[Shop] = []
staff: list[Staff] = []
product: list[Product] = []
productType: list[ProductType] = []
reptiles: list[Reptiles] = []
decoration: list[Decoration] = []