from abc import ABC, abstractmethod
from ..value_objects import Indirizzo

class Utente(ABC):

    def __init__(self, nome, cognome, sesso, nascita, via, civico, provincia, citta, cap, codice_fiscale):
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.nascita = nascita
        self.indirizzo = Indirizzo(via, civico, provincia, citta, cap, codice_fiscale)

    def __str__(self):
        return self.nome + " " + self.cognome
