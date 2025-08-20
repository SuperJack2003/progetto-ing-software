import datetime

from domain.attività.atleta import Atleta
from domain.attività.allenatore import Allenatore

class ContrattoAtletaAllenatore():
    def __init__(self, atleta: Atleta, allenatore: Allenatore, data: str):
        self._atleta = atleta
        self._allenatore = allenatore
        self._data = datetime.datetime.fromisoformat(data)

    def get_allenatore(self):
        return self._allenatore

    def get_atleta(self):
        return self._atleta

    def get_data(self):
        return self._data

    def __str__(self):
        return (f"Contratto tra l'allenatore: {self._allenatore.__str__()}"
                f" e l'atleta: {self._atleta.__str__()}")