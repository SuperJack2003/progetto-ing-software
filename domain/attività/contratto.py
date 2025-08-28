from abc import ABC, abstractmethod

class Contratto(ABC):

    _contatore_id = 0

    @classmethod
    def get_last_id(cls):
        return cls._contatore_id

    @classmethod
    def set_last_id(cls, last_id: int):
        cls._contatore_id = last_id

    @classmethod
    def assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self):
        self._id = Contratto.assegna_id()

    def get_id(self):
        return self._id