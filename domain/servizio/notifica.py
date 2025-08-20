import datetime

class Notifica:
    def __init__(self, nome: str, testo: str, id_destinatario: int, data: str):
        self._nome = nome
        self._testo = testo
        self._id_destinatario = id_destinatario
        self._data = datetime.datetime.fromisoformat(data)