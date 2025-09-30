class FasciaOraria:

    def __init__(self, giorno_settimana: str, orario_inizio: int, orario_fine: int):
        if giorno_settimana not in ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]:
            raise ValueError("Giorno della settimana non valido")
        if not 8 <= orario_inizio <= 19 or not 9 <= orario_fine <= 20 or orario_fine < orario_inizio:
            raise ValueError("Orario non valido")

        self._giorno_settimana = giorno_settimana
        self._orario_inizio = orario_inizio
        self._orario_fine = orario_fine

    def __str__(self):
        return f"{self._giorno_settimana} {self._orario_inizio}-{self._orario_fine}"

    def get_giorno_settimana(self):
        return self._giorno_settimana

    def get_orario_inizio(self):
        return self._orario_inizio

    def get_orario_fine(self):
        return self._orario_fine

class ProgrammazioneSettimanale:

    def __init__(self, lista_fasce_orarie: list[FasciaOraria]):
        self._lista_fascie_orarie = lista_fasce_orarie

    @classmethod
    def from_string(cls, stringa_orari: str):    #Stringa tipo: "Lunedì 18-20, Mercoledì 19-20"
        lista_fasce_orarie = []
        if not stringa_orari:
            return cls([])

        parti_orario = stringa_orari.split(",")
        for parte in parti_orario:
            try:
                elementi = parte.strip().split(" ")
                giorno = elementi[0]
                orari = elementi[1].strip().split("-")
                orario_inizio = int(orari[0])
                orario_fine = int(orari[1])
                lista_fasce_orarie.append(FasciaOraria(giorno, orario_inizio, orario_fine))
            except (ValueError, IndexError) as e:
                print(f"Errore: {e} in {parte.strip()}, verrà ignorata")
                continue

        return cls(lista_fasce_orarie)

    def controlla_giorno(self, giorno: str) -> bool:
        return any(fascia.get_giorno_settimana() == giorno for fascia in self._lista_fascie_orarie)

    def __str__(self):
        return ", ".join(str(fascia) for fascia in self._lista_fascie_orarie)