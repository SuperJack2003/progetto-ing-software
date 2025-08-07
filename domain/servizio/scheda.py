import datetime

class Scheda:

    _contatore_id = 0

    @classmethod
    def _assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, data_inizio: str):
        self._dataInizio = datetime.datetime.fromisoformat(data_inizio)
        self.id = Scheda._assegna_id()
        self.versione = 1
        self.lista_esercizi = []

    '''
    def aggiungi_esercizio_singolo(self, contratto_esercizio: contratto_esercizio):
        self._lista_esercizi.append(contratto_esercizio) 
    
    def aggiungi_esercizi_multipli(self, lista_esercizi: list):
        self.lista_esercizi.extend(lista_esercizi)
    '''
