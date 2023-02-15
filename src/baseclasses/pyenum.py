from enum import Enum


class Pyenum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
