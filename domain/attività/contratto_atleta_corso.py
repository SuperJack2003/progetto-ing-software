import datetime

from domain.attività.contratto import Contratto

class ContrattoAtletaCorso(Contratto):
    def __init__(self, id_atleta: int, id_corso: int, data: datetime.date):
        super().__init__()
        self._id_atleta = id_atleta
        self._id_corso = id_corso
        self.presenze = 0
        self._data_inizio = data

    def get_id_atleta(self):
        return self._id_atleta

    def get_id_corso(self):
        return self._id_corso

    def segna_presenza(self):
        self.presenze +=1
        return self.presenze

    def get_data(self):
        return self._data_inizio