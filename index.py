from service.animal import animal
import os

while True:
    os.system('clear||cls')
    print('0. Exit')
    print('1. Animal Database')
    print('2. Habitat Database')
    print('3. Location Database')
    choice = input('Enter Option: ')

    if choice == '0': 
        break

    if choice == '1':
        animal()