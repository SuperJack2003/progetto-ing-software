class Esercizio:
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

    def __init__(self, nome: str, descrizione: str, percorso_gif: str= None):
        self._nome = nome
        self._descrizione = descrizione
        self._percorso_gif = percorso_gif
        self._id = Esercizio._assegna_id()

    def get_nome(self):
        return self._nome

    def get_descrizione(self):
        return self._descrizione

    def get_percorso_gif(self):
        return self._percorso_gif

    def get_id(self):
        return self._id

    def set_descrizione(self, descrizione: str):
        self._descrizione = descrizione

    def set_percorso_gif(self, percorso_gif: str):
        self._percorso_gif = percorso_gif