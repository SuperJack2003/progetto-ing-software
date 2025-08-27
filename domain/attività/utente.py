from abc import ABC, abstractmethod
from ..value_objects import Indirizzo
import datetime

from domain.servizio.notifica import Notifica

class Utente(ABC):

    _contatore_id = 0

    @classmethod
    def _assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str= None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None):
        self._nome = nome
        self._cognome = cognome
        self._sesso = sesso
        self._nascita = datetime.datetime.fromisoformat(nascita)
        self._codice_fiscale = codice_fiscale
        self._indirizzo = Indirizzo(via, civico, provincia, citta, cap)
        self._telefono = telefono
        self._email = email
        self._id = Utente._assegna_id()
        self._lista_notifiche = []

    def __str__(self):
        return f"{self._nome} {self._cognome}"

    def get_eta(self):
        eta = datetime.date.today().year - self._nascita.year
        return eta

    def get_indirizzo(self):
        return self._indirizzo

    def get_id(self):
        return self._id

    def get_telefono(self):
        return self._telefono

    def get_email(self):
        return self._email

    def aggiungi_notifica(self, notifica: Notifica):
        self._lista_notifiche.append(notifica)

    @abstractmethod
    def get_ruolo(self):
        pass