import datetime

from domain.attività.allenatore import Allenatore
from domain.servizio.corso import Corso

class ContrattoAllenatoreCorso():
    def __init__(self, allenatore: Allenatore, corso: Corso, data: str):
        self._allenatore = allenatore
        self._corso = corso
        self._data = datetime.datetime.fromisoformat(data)

    def get_allenatore(self):
        return self._allenatore

    def get_corso(self):
        return self._corso

    def get_data(self):
        return self._data

    def __str__(self):
        return (f"Il corso {self._corso.get_nome()} è tenuto dall'allenatore "
                f"{self._allenatore.__str__()}")