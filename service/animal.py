import os
from database import animal as animalDatabase
from database import habitat as habitatDatabase
from models.Habitat import Habitat
from models.Reptiles import Reptiles
from models.Amphibian import Amphibian
from models.Mammal import Mammal
from models.Pisces import Pisces
from models.enums.PiscesGroup import PiscesGroup
from models.Arthropod import Arthropod
from models.Aves import Aves
from utilsFolder.info_template import getRandomIntroTemplate
from service.habitat import habitat

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
            # Check If Theres At Least 1 Habitat Available
            if len(habitatDatabase) == 0: 
                os.system('clear||cls')
                print('No Habitats Were Found, Please Create A New One...')
                input('Press Enter...')
                habitat()
                break
            
            while True:
                try:
                    os.system('clear||cls')
                    print('0. Back')
                    print('1. Reptile')
                    print('2. Amphibian')
                    print('3. Fish')
                    print('4. Mammal')
                    print('5. Bird')
                    print('6. Insect / Alike')

                    type = int(input('Type: '))

                    if type == 0: break

                    if not(1 <= type <= 6): raise Exception
                    
                    animalDatabase.append(addAnimal(type))
                    print('Animal Added Successfully')
                    input('Press Enter...')
                    break
                except:
                    print('Please Input Number Between 0 - 6')
                    input('Press Enter...')

        if choice == "2":
            os.system('clear||cls')
            if len(animalDatabase) == 0:
                print("No Animals Found")
            else:
                while True:
                    try:
                        print("0. Back")
                        showAnimal()
                        editAnimal = int(input("Choose Animal : "))
                        
                        if not(0 <= editAnimal <= len(animalDatabase)): 
                            raise Exception
                        if editAnimal == 0:
                            break

                        while True:
                            try:
                                os.system('clear||cls')
                                print('0. Back')
                                print('1. Reptile')
                                print('2. Amphibian')
                                print('3. Fish')
                                print('4. Mammal')
                                print('5. Bird')
                                print('6. Insect / Alike')

                                type = int(input('Type: '))

                                if type == 0: break

                                if not(1 <= type <= 6): raise Exception
                                
                                animalDatabase[editAnimal-1] = addAnimal(type)
                                print("Animal Edited")
                                break
                            except:
                                print('Please Input Number Between 0 - 6')
                        break
                    except:
                        print(f"Please Input Number between 0 - {len(animalDatabase)}")
            input('Press Enter...')

        if choice == "3":
            os.system('clear||cls')
            if len(animalDatabase) == 0:
                print("No Animals Found")
            else:
                while True:
                    try:
                        print("0. Back")
                        showAnimal()
                        while True:
                            try:
                                delAnimal = int(input("Choose Animal : "))
                                break
                            except:
                                print("Please Input Number...")

                        if delAnimal == 0:
                            break
                        if not(1 <= delAnimal <= len(animalDatabase)): 
                            raise Exception

                        animalDatabase.pop(delAnimal-1)
                        print("Animal Deleted")
                        break
                    except:
                        print(f"Please Input Number between 0 - {len(animalDatabase)}")
            input("Please Enter...")

        if choice == '4':
            os.system('clear||cls')
            if len(animalDatabase) == 0:
                print('No Animals Found')
            else:
                showAnimal()
            input('Press Enter...')
    
def addAnimal(type: int):
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
            weight = float(input('Weight (KG): '))
            break
        except:
            print('Please Input Number...')
    
    # Show All Habitats Available
    os.system('clear||cls')
    while True:
        try:
            n = 0

            for h in habitatDatabase:
                n += 1
                print(f'{n}. {h.name}')

            habitatId = int(input('Choose Habitat: '))
            if 1 <= habitatId <= n:
                break
            else:
                print(f'Please Input A Number Between 1 - {n}')
        except:
            print('Please Input Number...')

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
    
    if type == 1:
        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                hasShell = input('Has Shell?: ')
                if hasShell == '1':
                    hasShell = True
                elif hasShell == '2':
                    hasShell = False
                else:
                    raise Exception
                break
            except:
                print('Please Select From 1 To 2')
    
        newAnimal = Reptiles(scientificName, name, age, weight, habitatDatabase[habitatId-1]._id, isEndangered, getRandomIntroTemplate(), hasShell)

    elif type == 2:
        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                isPoisonous = input("Is it Poisonous ? : ")
                
                if isPoisonous == "1":
                    isPoisonous = True
                elif isPoisonous == "2":
                    isPoisonous = False
                else:
                    raise Exception
                break
            except:
                print("Please Select From 1 To 2 ")
        
        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                hasLegs = input("Has Legs ? : ")
                if hasLegs == "1":
                    hasLegs = True
                elif hasLegs == "2":
                    hasLegs = False
                else:
                    raise Exception
                break
            except:
                print("Please Select From 1 To 2 ")

        os.system('clear||cls')

        while True:
            try:
                numberOfLimbs = int(input("Number Of Limbs : "))
                break
            except:
                print('Please Input Number...')
        
        newAnimal = Amphibian(scientificName, name, age, weight, habitatDatabase[habitatId-1]._id, isEndangered, isPoisonous, hasLegs, numberOfLimbs, getRandomIntroTemplate())
    
    elif type == 3:
        os.system('clear||cls')

        while True:
            try:
                for member in PiscesGroup:
                    print(f"- {member.name}")
                group = input("Fish Group : ").upper()
                if group in PiscesGroup:
                    fishGroup = PiscesGroup[group]
                    print(f"Group set to {fishGroup.name}")
                else:
                    raise Exception
                break
            except:
                print("Group Not Found")

        input('Press Enter...')
        os.system('clear||cls')

        while True:
            try:
                length = int(input("Length (cm) : "))
                break
            except:
                print('Please Input Number...')

        newAnimal = Pisces(scientificName, name, age, weight, habitatDatabase[habitatId-1], isEndangered, length, fishGroup, getRandomIntroTemplate())

    elif type == 4:
        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                isNoctural = input("Is Nocturnal ? : ")
                if isNoctural == "1":
                    isNoctural = True
                elif isNoctural == "2":
                    isNoctural = False
                else:
                    raise Exception
                break
            except:
                print("Please Select From 1 To 2 ")

        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                isCarnivore = input("Is Carnivore ? : ")
                if isCarnivore == "1":
                    isCarnivore = True
                elif isCarnivore == "2":
                    isCarnivore = False
                else:
                    raise Exception
                break
            except:
                print("Please Select From 1 To 2 ")

        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                isHibernate = input("Can Hibernate ? : ")
                if isHibernate == "1":
                    isHibernate = True
                elif isHibernate == "2":
                    isHibernate = False
                else:
                    raise Exception
                break
            except:
                print("Please Select From 1 To 2 ")

        newAnimal = Mammal(scientificName, name, age, weight, habitatDatabase[habitatId-1]._id, isEndangered, isNoctural, isCarnivore, isHibernate, getRandomIntroTemplate())
    
    elif type == 5:
        os.system('clear||cls')
        print('1. Yes')
        print('2. No')

        while True:
            try:
                canFly = input("Can Fly ? : ")
                if canFly == "1":
                    canFly = True
                elif canFly == "2":
                    canFly = False
                else:
                    raise Exception
                break
            except:
                print("Please Select From 1 to 2")

        os.system('clear||cls')

        while True:
            try:
                wingspan = int(input("Wingspan (cm) : "))
                break
            except:
                print("Input Must Be a Number")

        newAnimal = Aves(scientificName, name, age, weight, habitatDatabase[habitatId-1], wingspan, canFly, isEndangered, getRandomIntroTemplate())

    elif type == 6:
        os.system('clear||cls')

        while True:
            try:
                numberOfLegs = int(input("Number Of Legs : "))
                break
            except:
                print('Please Input Number...')

        os.system('clear||cls')

        while True:
            try:
                numberOfMolts = int(input("Number Of Molts : "))
                break
            except:
                print('Please Input Number...')
        
        newAnimal = Arthropod(scientificName, name, age, weight, habitatDatabase[habitatId - 1], isEndangered, numberOfLegs, numberOfMolts, getRandomIntroTemplate())
    return newAnimal

def showAnimal():
    idx = 1
    for a in animalDatabase:
        print(f"{idx}. Name: {a.name}, Scientific Name: {a.scientificName}, Age: {a.age}")
        idx += 1