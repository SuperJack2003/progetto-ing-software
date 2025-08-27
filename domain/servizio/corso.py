class Corso:
    _contatore_id = 0

    @classmethod
    def assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, nome: str, orario_corso: str):
        self._nome = nome
        self._orario_corso = orario_corso
        self._stato = True
        self._lista_iscrizioni = []
        self._id_contratto_allenatore = None
        self._id = Corso.assegna_id()

    def get_lista_iscrizioni(self):
        return self._lista_iscrizioni

    def get_nome(self):
        return self._nome

    def get_orario_corso(self):
        return self._orario_corso

    def get_stato(self):
        return self._stato

    def get_contratto_allenatore(self):
        return self._id_contratto_allenatore

    def get_id(self):
        return self._id

    def aggiungi_iscritto(self, id_iscrizione: int):
        self._lista_iscrizioni.append(id_iscrizione)

    def assegna_allenatore(self, id_contratto_allenatore: int):
        self._id_contratto_allenatore = id_contratto_allenatore

    def set_orario_corso(self, orario_corso: str):
        self._orario_corso = orario_corso

    def set_status(self, status: bool):
        self._stato = status