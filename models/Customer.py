from models.enums.Gender import Gender

class Customer:
    def __init__(self, name: str, age: int, gender: Gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.isCheckOut = False