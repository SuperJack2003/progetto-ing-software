from abc import ABC, abstractmethod

class Contratto(ABC):

    contatore_id = 0

    @classmethod
    def assegna_id(cls):
        cls.contatore_id += 1
        return cls.contatore_id

    def __init__(self):
        self._id = Contratto.assegna_id()

    def get_id(self):
        return self._id