from datetime import datetime
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
from models.enums.Gender import Gender
from utilsFolder.info_template import getRandomIntroTemplate

staff: 'list[Staff]' = []
decoration: 'list[Decoration]' = []

# Design Pattern: Observer => Subscriber
sales: Sales = Sales([
    {
        'amount': 300000, 
        'productId': '8dda208f-2171-47ab-b847-d94412e7afaa',
        'customerId': 'ebbdc483-82a6-436e-809c-6a6318c97dc1',
        'date': datetime.now()
    }
])

location: 'list[Location]' = [
    Location('BLOCK A', 'This Is The Insects Section', 'block-a'),
    Location('BLOCK B', 'U Can See All Kind Of Fishes In This Area', 'block-b'),
    Location('BLOCK C', 'Birds Fly Freely In This Place', 'block-c'),
    Location('BLOCK D', 'This Is Where The Reptile Habitats', 'block-d'),
    Location('BLOCK E', 'Pandas, Zebras And Other Mammals Live Here', 'block-e'),
    Location('BLOCK F', 'Amphibians Dominated This Location', 'block-f'),
    Location('Park', 'Food Or Drink Stands Goes Here', 'park'),
    Location('Zoo Entrance', 'Get Your Zoo Ticket Here', 'zoo-entrance'),
]

shop: 'list[Shop]' = [
    Shop('zoo-entrance', ['8dda208f-2171-47ab-b847-d94412e7afaa'], 'Ticket Counter', 'c61195f6-c28b-46c1-b26d-17125573a378')
]

habitat: 'list[Habitat]' = [
    Habitat('block-e', 'Panda Habitat', 'c303282d-f2e6-46ca-a04a-35d3d873712d'),
    Habitat('block-e', 'Polar Bear Habitat', 'f9f8e918-e769-4c8d-89ef-2222abd520bf'),
    Habitat('block-c', 'Penguin Habitat', '7a1b19df-8651-4869-8023-13aedb389ce0'),
]

animal: 'list[Union[Aves, Amphibian, Arthropod, Mammal, Pisces, Reptiles]]' = [
    Mammal('Ailuropoda Melanoleuca', 'Giant Panda', 12, 90, 'c303282d-f2e6-46ca-a04a-35d3d873712d', True, False, True, False, getRandomIntroTemplate()),
    Mammal('Ursus Maritimus', 'Polar Bear', 16, 160, 'f9f8e918-e769-4c8d-89ef-2222abd520bf', True, True, True, False, getRandomIntroTemplate()),
    Aves('Spheniscus Mendiculus', 'Galapagos Penguin', 8, 2, '7a1b19df-8651-4869-8023-13aedb389ce0', 20, False, True, getRandomIntroTemplate()),
    Aves('Pygoscelis Adeliae', 'Adelie Penguin', 6, 5, '7a1b19df-8651-4869-8023-13aedb389ce0', 50, False, False, getRandomIntroTemplate()),
    Aves('Pygoscelis Papua', 'Gentoo Penguin', 10, 5, '7a1b19df-8651-4869-8023-13aedb389ce0', 60, False, False, getRandomIntroTemplate()),
]

productType: 'list[ProductType]' = [
    ProductType('Soda', 'soda'),
    ProductType('Cold Drink', 'cold-drink'),
    ProductType('Frozen Food', 'frozen-food'),
    ProductType('Snack', 'snack'),
    ProductType('Accessory', 'accessory'),
    ProductType('Ticket', 'ticket')
]

product: 'list[Product]' = [
    Product('Zoo Ticket', 300000, 1000, 'ticket', '8dda208f-2171-47ab-b847-d94412e7afaa'),
    Product('Coca Cola', 8000, 60, 'soda', '6b59f7eb-0b81-45a7-beeb-23b55c336386'),
    Product('NESCAFÉ', 10000, 100, 'cold-drink', '034fad5f-3e56-44fd-b158-338de4af43d7'),
    Product('Dr. Pepper', 9000, 80, 'soda', '3237c7eb-f8b3-4945-bffe-07946db930dd'),
]

facility: 'list[Facility]' = [
    Facility('Vending Machine', 'park', ['6b59f7eb-0b81-45a7-beeb-23b55c336386', '034fad5f-3e56-44fd-b158-338de4af43d7', '3237c7eb-f8b3-4945-bffe-07946db930dd'])
]

customer: 'list[Customer]' = [
    Customer('Crystal Jade', 22, Gender.FEMALE, 'ebbdc483-82a6-436e-809c-6a6318c97dc1')
]