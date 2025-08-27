import datetime
from dateutil.relativedelta import relativedelta

from domain.attività.contratto import Contratto

class ContrattoAbbonamento(Contratto):

    def __init__(self, id_atleta: int, id_abbonamento: int, durata: int, tipologia: str, data: datetime.date):
        super().__init__()
        self._atleta = id_atleta
        self._abbonamento = id_abbonamento
        self._tipologia = tipologia
        self._data_inizio = data
        self._durata = durata
        self._scadenza = self._data_inizio + relativedelta(months=durata)

    def get_atleta(self):
        return self._atleta

    def get_abbonamento(self):
        return self._abbonamento

    def get_tipologia(self):
        return self._tipologia

    def get_data(self):
        return self._data_inizio

    def get_scadenza(self):
        return self._scadenza