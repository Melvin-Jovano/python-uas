import uuid

class Location:
    def __init__(self, name: str, description: bool) -> None:
        self._id = str(uuid.uuid4())
        self.name = name
        self.description = description