from models.Animal import Animal
import os

def animal():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Animal')
        print('2. Edit Animal')
        print('3. Delete Animal')
        print('4. Show All Animal')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')
            scientificName = input('Scientific Name: ')
            name = input('Animal Name: ')
            age = input('Age: ')
            weight = input('Weight: ')

            # TODO Show Habitat List
            habitatId = input('Habitat: ')

            os.system('clear||cls')
            print('1. Yes')
            print('2. No')
            isEndangered = input('Is It Endangered?: ')