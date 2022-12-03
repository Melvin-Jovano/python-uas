from models.Animal import Animal
import os
from database import animal as animalDatabase

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

            while True:
                try:
                    age = int(input('Age: '))
                    break
                except:
                    print('Please Input Number...')

            while True:
                try:
                    weight = int(input('Weight (KG): '))
                    break
                except:
                    print('Please Input Number...')
            

            os.system('clear||cls')
            # TODO Show Habitat List
            habitatId = input('Habitat: ')

            os.system('clear||cls')
            print('1. Yes')
            print('2. No')

            while True:
                try:
                    isEndangered = input('Is It Endangered?: ')
                    if isEndangered == '1':
                        isEndangered = True
                    elif isEndangered == '2':
                        isEndangered = False
                    else:
                        raise Exception
                    break
                except:
                    print('Please Select From 1 To 2')
            
            animalDatabase.append(Animal(scientificName, name, age, weight, habitatId, isEndangered))

        if choice == '4':
            for a in animalDatabase:
                print(f'ID: {a._id}, Name: {a.name}')
            input('Press Enter...')
    