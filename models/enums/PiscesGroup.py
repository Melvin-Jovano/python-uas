from enum import Enum, EnumMeta

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True
    
class BaseEnum(Enum, metaclass = MetaEnum):
    pass

class PiscesGroup(BaseEnum):
    BONY = "BONY"
    CATILAGIOUS = "CATILAGIOUS"
    LAMPREY = "LAMPREY"