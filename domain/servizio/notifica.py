import datetime

class Notifica:
    def __init__(self, nome: str, testo: str, id_destinatario: int, data: str):
        self._nome = nome
        self._testo = testo
        self._id_destinatario = id_destinatario
        self._data = datetime.datetime.fromisoformat(data)

    def get_id_destinatario(self):
        return self._id_destinatario

    def get_nome(self):
        return self._nome

    def get_testo(self):
        return self._testo

    def get_data(self):
        return self._data