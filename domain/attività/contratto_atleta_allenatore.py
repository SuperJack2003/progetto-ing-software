import datetime

from domain.attività.contratto import Contratto

class ContrattoAtletaAllenatore(Contratto):
    def __init__(self, id_atleta: int, id_allenatore: int, data: datetime.date):
        super().__init__()
        self._id_atleta = id_atleta
        self._id_allenatore = id_allenatore
        self._data_inizio = data

    def get_allenatore(self):
        return self._id_allenatore

    def get_atleta(self):
        return self._id_atleta

    def get_data(self):
        return self._data_inizio