import datetime

from domain.attività.atleta import Atleta
from domain.servizio.corso import Corso

class ContrattoAtletaCorso():
    def __init__(self, atleta: Atleta, corso: Corso, data: str):
        self._atleta = atleta
        self._corso = corso
        self.presenze = 0
        self._data = datetime.datetime.fromisoformat(data)

    def get_atleta(self):
        return self._atleta

    def get_corso(self):
        return self._corso

    def segna_presenza(self):
        self.presenze +=1
        return self.presenze

    def get_data(self):
        return self._data

    def __str__(self):
        return f"L'atleta {self._atleta.__str__()} è iscritto al corso {self._corso.get_nome()}"
