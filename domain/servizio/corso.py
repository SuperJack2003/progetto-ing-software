class Corso:
    _contatore_id = 0

    @classmethod
    def get_last_id(cls):
        return cls._contatore_id

    @classmethod
    def set_last_id(cls, last_id: int):
        cls._contatore_id = last_id

    @classmethod
    def assegna_id(cls):
        cls._contatore_id += 1
        return cls._contatore_id

    def __init__(self, nome: str, descrizione: str, eta_min: int, eta_max: int, orario_corso: str):
        self._nome = nome
        self._descrizione = descrizione
        self._eta_min = eta_min
        self._eta_max = eta_max
        self._orario_corso = orario_corso
        self._stato = True
        self._lista_iscrizioni = []
        self._id_contratto_allenatore = None
        self._id = Corso.assegna_id()

    def get_lista_iscrizioni(self):
        return self._lista_iscrizioni

    def get_nome(self):
        return self._nome

    def get_descrizione(self):
        return self._descrizione

    def get_fascia_eta(self):
        return f"{self._eta_min} - {self._eta_max}"

    def get_eta_min(self):
        return self._eta_min

    def get_eta_max(self):
        return self._eta_max

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