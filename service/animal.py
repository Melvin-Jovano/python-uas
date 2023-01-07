import os
from database import animal as animalDatabase
from database import habitat as habitatDatabase
from utilsFolder.text_style import TextStyle
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

        choice = input('\nEnter Option: ')

        if choice == '0': break

        if choice == '1':
            # Check If Theres At Least 1 Habitat Available
            if len(habitatDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Habitats Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
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

                    type = int(input('\nType: '))

                    if type == 0: break

                    if not(1 <= type <= 6): raise Exception
                    
                    animalDatabase.append(addAnimal(type))
                    os.system('clear||cls')
                    print(f'{TextStyle.GREEN}Animal Added Successfully{TextStyle.END}')
                    input('\nPress Enter...')
                    break
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number Between 0 - 6{TextStyle.END}')
                    input('\nPress Enter...')

        if choice == "2":
            if len(animalDatabase) == 0:
                os.system('clear||cls')
                print(f"\n{TextStyle.RED}No Animals Found{TextStyle.END}")
                input('\nPress Enter...')
            else:
                while True:
                    try:
                        os.system('clear||cls')
                        print("0. Back")
                        showAnimal()
                        editIdx = int(input("\nChoose Animal : "))

                        if not(0 <= editIdx <= len(animalDatabase)): 
                            raise Exception
                        if editIdx == 0:
                            break        
                        os.system("cls||clear")
                        while True:
                            editAnimal(animalDatabase[editIdx-1])  
                            os.system('clear||cls')
                            print(f"{TextStyle.GREEN}Animal Edited{TextStyle.END}")
                            input('\nPress Enter...')
                            break
                        break
                    except:
                        os.system('clear||cls')
                        print(f"\nPlease Input Number between 0 - {len(animalDatabase)}")
                        input('\nPress Enter...')

        if choice == "3":
            os.system('clear||cls')
            if len(animalDatabase) == 0:
                os.system('clear||cls')
                print(f"\n{TextStyle.RED}No Animals Found{TextStyle.END}")
                input('\nPress Enter...')
            else:
                while True:
                    try:
                        print("0. Back")
                        showAnimal()
                        while True:
                            try:
                                delAnimal = int(input("\nChoose Animal : "))
                                break
                            except:
                                os.system('clear||cls')
                                print(f"\n{TextStyle.RED}Please Input Number...{TextStyle.END}")
                                input('\nPress Enter...')

                        if delAnimal == 0:
                            break
                        if not(1 <= delAnimal <= len(animalDatabase)): 
                            raise Exception

                        animalDatabase.pop(delAnimal-1)

                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Animal Deleted{TextStyle.END}")
                        input('\nPress Enter...')
                        break
                    except:
                        os.system('clear||cls')
                        print(f"\n{TextStyle.RED}Please Input Number between 0 - {len(animalDatabase)}{TextStyle.END}")
                        input('\nPress Enter...')

        if choice == '4':
            if len(animalDatabase) == 0:
                os.system('clear||cls')
                print(f'\n{TextStyle.RED}No Animals Found{TextStyle.END}')
                input('\nPress Enter...')
            else:
                os.system('clear||cls')
                showAnimal()
                input('\nPress Enter...')
    
def addAnimal(type: int):
    os.system('clear||cls')
    scientificName = input('Scientific Name: ')

    os.system('clear||cls')
    name = input('Animal Name: ')

    while True:
        try:
            os.system('clear||cls')
            age = int(input('Age: '))
            break
        except:
            os.system('clear||cls')
            print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
            input('\nPress Enter...')

    while True:
        try:
            os.system('clear||cls')
            weight = float(input('Weight (KG): '))
            break
        except:
            os.system('clear||cls')
            print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
            input('\nPress Enter...')
    
    # Show All Habitats Available
    os.system('clear||cls')
    while True:
        try:
            os.system('clear||cls')
            n = 0

            for h in habitatDatabase:
                n += 1
                print(f'{n}. {h.name}')

            habitatId = int(input('\nChoose Habitat: '))
            if 1 <= habitatId <= n:
                break
            else:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input A Number Between 1 - {n}{TextStyle.END}')
                input('\nPress Enter...')
        except:
            os.system('clear||cls')
            print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
            input('\nPress Enter...')

    while True:
        try:
            os.system('clear||cls')
            print('1. Yes')
            print('2. No')
            isEndangered = input('\nIs It Endangered?: ')
            if isEndangered == '1':
                isEndangered = True
            elif isEndangered == '2':
                isEndangered = False
            else:
                raise Exception
            break
        except:
            os.system('clear||cls')
            print(f'{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}')
            input('\nPress Enter...')
    
    if type == 1:
        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                hasShell = input('\nHas Shell?: ')
                if hasShell == '1':
                    hasShell = True
                elif hasShell == '2':
                    hasShell = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}')
                input('\nPress Enter...')
    
        newAnimal = Reptiles(scientificName, name, age, weight, habitatDatabase[habitatId-1]._id, isEndangered, getRandomIntroTemplate(), hasShell)

    elif type == 2:
        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                isPoisonous = input("\nIs it Poisonous ? : ")
                if isPoisonous == "1":
                    isPoisonous = True
                elif isPoisonous == "2":
                    isPoisonous = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}")
                input('\nPress Enter...')
        
        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                hasLegs = input("\nHas Legs ? : ")
                if hasLegs == "1":
                    hasLegs = True
                elif hasLegs == "2":
                    hasLegs = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}")
                input('\nPress Enter...')

        while True:
            try:
                os.system('clear||cls')
                numberOfLimbs = int(input("Number Of Limbs : "))
                break
            except:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                input('\nPress Enter...')
        
        newAnimal = Amphibian(scientificName, name, age, weight, habitatDatabase[habitatId-1]._id, isEndangered, isPoisonous, hasLegs, numberOfLimbs, getRandomIntroTemplate())
    
    elif type == 3:
        while True:
            try:
                os.system('clear||cls')
                for member in PiscesGroup:
                    print(f"- {member.name}")
                group = input("\nFish Group : ").upper()
                if group in PiscesGroup:
                    fishGroup = PiscesGroup[group]
                    os.system('clear||cls')
                    print(f"{TextStyle.GREEN}Group Set To {fishGroup.name}{TextStyle.END}")
                    input('\nPress Enter...')
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Group Not Found{TextStyle.END}")
                input('\nPress Enter...')

        while True:
            try:
                os.system('clear||cls')
                length = float(input("Length (cm) : "))
                break
            except:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                input('\nPress Enter...')

        newAnimal = Pisces(scientificName, name, age, weight, habitatDatabase[habitatId-1], isEndangered, length, fishGroup, getRandomIntroTemplate())

    elif type == 4:
        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                isNoctural = input("\nIs Nocturnal ? : ")
                if isNoctural == "1":
                    isNoctural = True
                elif isNoctural == "2":
                    isNoctural = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}")
                input('\nPress Enter...')

        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                isCarnivore = input("\nIs Carnivore ? : ")
                if isCarnivore == "1":
                    isCarnivore = True
                elif isCarnivore == "2":
                    isCarnivore = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}")
                input('\nPress Enter...')
        
        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                isHibernate = input("\nCan Hibernate ? : ")
                if isHibernate == "1":
                    isHibernate = True
                elif isHibernate == "2":
                    isHibernate = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Please Select From 1 To 2{TextStyle.END}")
                input('\nPress Enter...')

        newAnimal = Mammal(scientificName, name, age, weight, habitatDatabase[habitatId-1]._id, isEndangered, isNoctural, isCarnivore, isHibernate, getRandomIntroTemplate())
    
    elif type == 5:
        while True:
            try:
                os.system('clear||cls')
                print('1. Yes')
                print('2. No')
                canFly = input("\nCan Fly ? : ")
                if canFly == "1":
                    canFly = True
                elif canFly == "2":
                    canFly = False
                else:
                    raise Exception
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Please Select From 1 to{TextStyle.END}")
                input('\nPress Enter...')

        while True:
            try:
                os.system('clear||cls')
                wingspan = float(input("Wingspan (cm) : "))
                break
            except:
                os.system('clear||cls')
                print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                input('\nPress Enter...')

        newAnimal = Aves(scientificName, name, age, weight, habitatDatabase[habitatId-1], wingspan, canFly, isEndangered, getRandomIntroTemplate())

    elif type == 6:
        while True:
            try:
                os.system('clear||cls')
                numberOfLegs = int(input("Number Of Legs : "))
                break
            except:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                input('\nPress Enter...')

        while True:
            try:
                os.system('clear||cls')
                numberOfMolts = int(input("Number Of Molts : "))
                break
            except:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                input('\nPress Enter...')
        
        newAnimal = Arthropod(scientificName, name, age, weight, habitatDatabase[habitatId - 1], isEndangered, numberOfLegs, numberOfMolts, getRandomIntroTemplate())
    return newAnimal

def editAnimal(animalObj: object):
    while True:
        try:
            os.system('clear||cls')
            age = input('Age: ')
            animalObj.age = int(age)
            break
        except:
            if age.strip() == "":
                break
            else:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                input('\nPress Enter...')

    while True:
        try:
            os.system('clear||cls')
            weight = input('Weight (KG): ')
            animalObj.weight = float(weight)
            break
        except:
            if weight.strip() == "":
                break
            else:
                os.system('clear||cls')
                print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                input('\nPress Enter...')

    if isinstance(animalObj, Reptiles):
        while True:
            try:
                os.system('clear||cls')
                numberOfEggs = input('Number of Eggs : ')
                animalObj.numberOfEggs = int(numberOfEggs)
                break
            except:
                if numberOfEggs.strip() == "":
                    break
                else:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                    input('\nPress Enter...')

    elif isinstance(animalObj, Amphibian):
        while True:
            try:
                os.system('clear||cls')
                numberOfLimbs = input("Number of Limbs : ")
                animalObj.numberOfLimbs = int(numberOfLimbs)
                break
            except:
                if numberOfLimbs.strip() == "":
                    break
                else:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                    input('\nPress Enter...')

    elif isinstance(animalObj, Pisces):
        while True:
            try:
                os.system('clear||cls')
                length = input("Length (cm) : ")
                animalObj.length = float(length)
                break
            except:
                if length.strip() == "":
                    break
                else:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number...{TextStyle.END}')
                    input('\nPress Enter...')

    elif isinstance(animalObj, Mammal):
        while True:
            try:
                os.system('clear||cls')
                print("1. Start")
                print("2. End")
                hibernateInput = input("\nHibernation : ")
                hibernate = int(hibernateInput)
                
                if hibernate == 1:
                    animalObj.isHibernate = True
                elif hibernate == 2:
                    animalObj.isHibernate = False
                else:
                    raise Exception
                break
            except:
                if hibernateInput.strip() == "":
                    break
                else:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Please Select From 0 to 2{TextStyle.END}")
                    input('\nPress Enter...')

    elif isinstance(animalObj, Aves):
        while True:
            try:
                os.system('clear||cls')
                wingspan = input("Wingspan (cm) : ")
                animalObj.wingspan = float(wingspan)
                break
            except:
                if wingspan.strip() == "":
                    break
                else:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Please Input Number...{TextStyle.END}")
                    input('\nPress Enter...')

    elif isinstance(animalObj, Arthropod):
        while True:
            try:
                os.system('clear||cls')
                numberOfMolts = input("Number of Molts : ")
                animalObj.numberOfMolts = int(numberOfMolts)
                break
            except:
                if numberOfMolts.strip() == "":
                    break
                else:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Please Input Number...{TextStyle.END}")
                    input('\nPress Enter...')

def showAnimal():
    idx = 1
    ignore_keys = {"_id", "habitatId", "introTemplate"}
    for a in animalDatabase:
        print(f"\n{idx}", end=". ")
        for key, val in a.printData().items():
            if key not in ignore_keys:
                if key == "scientificName":
                    print(f"{key} : {str(val).ljust(25)}", end=", ")
                elif key == "name":
                    print(f"{key} : {str(val).ljust(20)}", end=", ")
                else:
                    print(f"{key} : {str(val).rjust(5)}", end=", ")
        idx += 1
    print("")