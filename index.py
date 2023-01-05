from service.animal import animal
from service.customer import customer
from service.decoration import decoration
from service.habitat import habitat
from service.product import product
from service.facility import facility
from database import facility as facilityDatabase
import os
from service.sales_report import salesReport
from service.sell_product import sellProduct
from service.shop import shop

while True:
    os.system('clear||cls')
    print('0. Exit')
    print('1. Animal Database')
    print('2. Habitat Database')
    print('3. Product Database')
    print('4. Facility Database')
    print('5. Shop Database')
    print('6. Customer Database')
    print('7. Decoration Database')
    print('8. Sell Product')
    print('9. Sales Report')

    choice = input('\nEnter Option: ')

    if choice == '0': 
        os.system('clear||cls')
        print('App Closed')
        break

    if choice == '1':
        animal()

    if choice == '2':
        habitat()

    if choice == '3':
        product()

    if choice == '4':
        facility()

    if choice == '5':
        shop()

    if choice == '6':
        customer()
    
    if choice == '7':
        decoration()

    if choice == '8':
        sellProduct()

    if choice == '9':
        salesReport()