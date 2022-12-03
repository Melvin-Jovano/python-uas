from service.animal import animal
from service.habitat import habitat
import os

while True:
    os.system('clear||cls')
    print('0. Exit')
    print('1. Animal Database')
    print('2. Habitat Database')
    choice = input('Enter Option: ')

    if choice == '0': 
        os.system('clear||cls')
        print('App Closed')
        break

    if choice == '1':
        animal()

    if choice == '2':
        habitat()