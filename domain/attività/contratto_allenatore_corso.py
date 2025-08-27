import datetime

from domain.attività.contratto import Contratto

class ContrattoAllenatoreCorso(Contratto):
    def __init__(self, id_allenatore: int, id_corso: int, data: datetime.date):
        super().__init__()
        self._id_allenatore = id_allenatore
        self._id_corso = id_corso
        self._data = data

    def get_allenatore(self):
        return self._id_allenatore

    def get_corso(self):
        return self._id_corso

    def get_data(self):
        return self._data