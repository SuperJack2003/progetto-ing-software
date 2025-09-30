from domain.value_objects.programmazione import ProgrammazioneSettimanale

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

    def __init__(self, nome: str, descrizione: str, eta_min: int, eta_max: int, orari_corso: str):
        self._nome = nome
        self._descrizione = descrizione
        self._eta_min = eta_min
        self._eta_max = eta_max
        self._programmazione_settimanale = ProgrammazioneSettimanale.from_string(orari_corso)
        self._stato = True
        self._id = Corso.assegna_id()

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

    def get_programmazione_settimanale(self) -> ProgrammazioneSettimanale:
        return self._programmazione_settimanale

    def get_stato(self):
        return self._stato

    def get_id(self):
        return self._id

    def set_orario_corso(self, orario_corso: str):
        self._programmazione_settimanale = ProgrammazioneSettimanale.from_string(orario_corso)

    def set_stato(self, stato: bool):
        self._stato = stato