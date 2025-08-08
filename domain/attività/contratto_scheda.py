import datetime
from dateutil.relativedelta import relativedelta

from domain.attività.atleta import Atleta
from domain.servizio.scheda import Scheda

class ContrattoScheda():
    def __init__(self, atleta: Atleta, scheda: Scheda, durata: int, data: str):
        self._atleta = atleta
        self._scheda = scheda
        self._durata = durata
        self._stato = False
        self._data = datetime.datetime.fromisoformat(data)
        self._scadenza = self.calcola_scadenza()

    def calcola_scadenza(self):
        scadenza = self._data + relativedelta(months=self._durata)
        return scadenza

    def get_atleta(self):
        return self._atleta

    def get_scheda(self):
        return self._scheda

    def get_stato(self):
        return self._stato
