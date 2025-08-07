from abc import ABC, abstractmethod
from ..value_objects import Indirizzo
import datetime

class Utente(ABC):
    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str= None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None):
        self._nome = nome
        self._cognome = cognome
        self._sesso = sesso
        self._nascita = datetime.datetime.fromisoformat(nascita)
        self._codice_fiscale = codice_fiscale
        self._indirizzo = Indirizzo(via, civico, provincia, citta, cap)

    def __str__(self):
        return f"{self._nome} {self._cognome}"

    def getEta(self):
        eta = datetime.date.today().year - self._nascita.year
        return eta

    def getIndirizzo(self):
        return self._indirizzo

    @abstractmethod
    def getRuolo(self):
        pass