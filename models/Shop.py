import uuid


class Shop:
    locationId: int = 0
    productId: int = 0
    name: str = ''

    def __init__(self, locationId: int, productId: int, name: str) -> None:
        self._id = str(uuid.uuid4())
        self.locationId = locationId
        self.productId = productId
        self.name = name
