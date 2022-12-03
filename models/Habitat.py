import uuid

class Habitat:
    def __init__(self, locationId: str, name: str) -> None:
        self._id = str(uuid.uuid4())
        self.locationId = locationId
        self.name = name