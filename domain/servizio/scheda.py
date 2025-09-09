import datetime

class Scheda:

    _contatore_id = 0

    @classmethod
    def get_last_id(cls):
        return cls._contatore_id

    @classmethod
    def set_last_id(cls, last_id: int):
        cls._contatore_id = last_id

    @classmethod
    def _assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, id_allenatore: int, data: datetime.date):
        self._data_creazione = data
        self._id_allenatore = id_allenatore
        self._id = Scheda._assegna_id()
        self._lista_esercizi = []

    def get_data_creazione(self):
        return self._data_creazione

    def get_id_allenatore(self):
        return self._id_allenatore

    def get_lista_esercizi(self):
        return self._lista_esercizi

    def get_id(self):
        return self._id

    def aggiungi_esercizio(self, id_contratto_esercizio: int):
        self._lista_esercizi.append(id_contratto_esercizio)
    
    def aggiungi_esercizi(self, lista_esercizi: list[int]):
        self._lista_esercizi.extend(lista_esercizi)