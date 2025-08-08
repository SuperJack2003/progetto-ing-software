import datetime

class Notifica:
    def __init__(self, nome, testo, idDestinatario):
        self._nome = nome
        self._testo = testo
        self._idDestinatario = idDestinatario
        self._data = datetime.datetime.now()