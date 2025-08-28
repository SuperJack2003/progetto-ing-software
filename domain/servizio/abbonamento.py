class Abbonamento:
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

    def __init__(self, durata: int, tipo: str):
        self._durata = durata
        self._tipo = tipo
        self._id = Abbonamento.assegna_id()

    def get_durata(self):
        return self._durata

    def get_tipo(self):
        return self._tipo

    def get_id(self):
        return self._id

    def get_nome(self):
        return f"{self._durata}-{self._tipo}" #Es. Nome: 2-corsi+sala

    def __str__(self):
        return f"{self._durata} mesi, {self._tipo}"
