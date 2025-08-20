import datetime

from domain.servizio.scheda import Scheda
from domain.servizio.esercizio import Esercizio

class ContrattoEsercizio():
    def __init__(self, esercizio: Esercizio, scheda: Scheda, data: str, serie: int,
                 ripetizioni: int, recupero: int, modalita: str=""):
        self._esercizio = esercizio
        self._scheda = scheda
        self._serie = serie
        self._ripetizioni = ripetizioni
        self._recupero = recupero
        self._modalita = modalita
        self._data = datetime.datetime.fromisoformat(data)

    def get_esercizio(self):
        return self._esercizio

    def get_scheda(self):
        return self._scheda

    def __str__ (self):
        return (f"Svolgere {self._esercizio.get_nome()} {self._serie}X{self._ripetizioni} "
                f"con {self._recupero}s recupero. {self._modalita}")