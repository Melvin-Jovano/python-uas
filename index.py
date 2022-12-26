from service.animal import animal
from service.customer import customer
from service.habitat import habitat
from service.product import product
from service.facility import facility
from database import facility as facilityDatabase
import os
from service.sales_report import salesReport
from service.sell_product import sellProduct

while True:
    os.system('clear||cls')
    print('0. Exit')
    print('1. Animal Database')
    print('2. Habitat Database')
    print('3. Product Database')
    print('4. Facility Database')
    print('5. Customer Database')
    print('6. Sell Product')
    print('7. Sales Report')

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
        customer()

    if choice == '6':
        sellProduct()

    if choice == '7':
        salesReport()