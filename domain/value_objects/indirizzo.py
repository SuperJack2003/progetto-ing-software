class Indirizzo:
    def __init__(self, via, civico, provincia, citta, cap):
        self._via = via
        self._civico = civico
        self._provincia = provincia
        self._citta = citta
        self._cap = cap

    def __str__(self):
        return f"{self._via} {self._civico}, {self._citta} {self._provincia} {self._cap}"

    def get_via(self):
        return self._via

    def get_civico(self):
        return self._civico

    def get_privincia(self):
        return self._provincia

    def get_citta(self):
        return self._citta

    def get_cap(self):
        return self._cap