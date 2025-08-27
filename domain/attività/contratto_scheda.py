import datetime
from dateutil.relativedelta import relativedelta

from domain.attività.contratto import Contratto

class ContrattoScheda(Contratto):
    def __init__(self, id_atleta: int, id_scheda: int, id_creatore: int, durata: int, data: datetime.date):
        super().__init__()
        self._id_atleta = id_atleta
        self._id_scheda = id_scheda
        self._id_creatore = id_creatore
        self._durata = durata
        self._stato = False
        self._data_inizio = data
        self._scadenza = self.calcola_scadenza()

    def calcola_scadenza(self):
        scadenza = self._data_inizio + relativedelta(months=self._durata)
        return scadenza

    def get_atleta(self):
        return self._id_atleta

    def get_scheda(self):
        return self._id_scheda

    def get_creatore(self):
        return self._id_creatore

    def get_stato(self):
        return self._stato

    def set_stato(self, stato: bool):
        self._stato = stato