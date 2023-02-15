from enum import Enum
from src.baseclasses.pyenum import Pyenum


class Genders(Enum):
    FEMALE = "female"
    MALE = "male"

class Statuses(Pyenum):
    INACTIVE = "inactive"
    ACTIVE = "active"
