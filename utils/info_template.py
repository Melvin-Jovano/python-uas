from models.Animal import Animal

def defaultIntro(animal: Animal):
    if animal.isEndangered:
        return f'{animal.name}, {animal.age} Years Old, And Sadly Im Endangered.'
    else:
        return f'{animal.name}, {animal.age} Years Old, And Im Not Endangered, phew.'

def fancyIntro(animal: Animal):
    return f'Whats Cooking Good Looking, People Call Me {animal.name} But U Can Call Me {animal.scientificName}.'

def slayIntro(animal: Animal):
    return f'Step Aside, Cuz A Cool {animal.weight}KG {animal.name} Has Appeared.'

def askIntro(animal: Animal):
    return f'Have U Seen A Gorgeus {animal.name} Pass By? Oh Wait Thats Me.'