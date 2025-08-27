import datetime

from domain.attività.contratto import Contratto

class ContrattoEsercizio(Contratto):
    def __init__(self, id_esercizio: int, id_scheda: int, data: datetime.date, serie: int,
                 ripetizioni: int, recupero: int, modalita: str=""):
        super().__init__()
        self._id_esercizio = id_esercizio
        self._id_scheda = id_scheda
        self._serie = serie
        self._ripetizioni = ripetizioni
        self._recupero = recupero
        self._modalita = modalita
        self._data_inizio = data

    def get_esercizio(self):
        return self._id_esercizio

    def get_scheda(self):
        return self._id_scheda

    def get_serie(self):
        return self._serie

    def get_ripetizioni(self):
        return self._ripetizioni

    def get_recupero(self):
        return self._recupero

    def get_modalita(self):
        return self._modalita

    def get_data_inizio(self):
        return self._data_inizio