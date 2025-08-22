class Abbonamento:
    def __init__(self, durata: int, tipo: str):
        self._durata = durata
        self._tipo = tipo

    def get_durata(self):
        return self._durata

    def get_tipo(self):
        return self._tipo

    def get_nome(self):
        return f"{self._durata}-{self._tipo}" #Es. Nome: 2-corsi+sala

    def __str__(self):
        return f"{self._durata} mesi, {self._tipo}"
