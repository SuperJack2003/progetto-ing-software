import datetime

from domain.attività.contratto_esercizio import ContrattoEsercizio

class Scheda:

    _contatore_id = 0

    @classmethod
    def _assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, id_allenatore: int, data: str):
        self._data_creazione = datetime.datetime.fromisoformat(data)
        self._id_allenatore = id_allenatore
        self._id = Scheda._assegna_id()
        self._versione = 1
        self._lista_esercizi = []

    def get_data(self):
        return self._data_creazione

    def aggiungi_esercizio_singolo(self, contratto_esercizio: ContrattoEsercizio):
        self._lista_esercizi.append(contratto_esercizio) 
    
    def aggiungi_esercizi_multipli(self, lista_esercizi: list):
        self._lista_esercizi.extend(lista_esercizi)

