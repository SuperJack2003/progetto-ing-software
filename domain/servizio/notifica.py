import datetime

class Notifica:
    _contatore_id = 0

    @classmethod
    def assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, nome: str, testo: str, id_destinatario: int, data: datetime.date):
        self._nome = nome
        self._testo = testo
        self._id_destinatario = id_destinatario
        self._data = data
        self._id = Notifica.assegna_id()

    def get_id_destinatario(self):
        return self._id_destinatario

    def get_nome(self):
        return self._nome

    def get_testo(self):
        return self._testo

    def get_data(self):
        return self._data

    def get_id(self):
        return self._id