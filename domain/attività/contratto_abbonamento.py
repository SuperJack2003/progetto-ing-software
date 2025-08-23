import datetime
from dateutil.relativedelta import relativedelta

from domain.attività.atleta import Atleta
from domain.servizio.abbonamento import Abbonamento

class ContrattoAbbonamento():
    def __init__(self, atleta: Atleta, abbonamento: Abbonamento, data: str):
        self._atleta = atleta
        self._abbonamento = abbonamento
        self._scadenza = self._calcola_scadenza()
        self._data = datetime.datetime.fromisoformat(data)

    def _calcola_scadenza(self):
        scadenza = self._data + relativedelta(months=self._abbonamento.get_durata())
        return scadenza

    def get_atleta(self):
        return self._atleta

    def get_abbonamento(self):
        return self._abbonamento

    def get_data(self):
        return self._data

    def get_scadenza(self):
        return self._scadenza

    def __str__(self):
        return (f"{self._atleta.__str__()} ha un abbonamento: {self._abbonamento.__str__()} in scadenza"
                f"{self._scadenza}")