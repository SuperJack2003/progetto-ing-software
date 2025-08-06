class Indirizzo:
    def __init__(self, via, civico, provincia, citta, cap, codice_fiscale):
        self.via = via
        self.civico = civico
        self.provincia = provincia
        self.citta = citta
        self.cap = cap
        self.codice_fiscale = codice_fiscale

    def __str__(self):
        return (self.via + " " +  self.civico + " " + self.provincia + " "
                        + " " + self.citta + " " + self.cap)