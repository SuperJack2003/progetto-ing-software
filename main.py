from domain.attività.allenatore import Allenatore
from domain.attività.atleta import Atleta

def main():
    utente = Atleta("Giacomo", "Cipolletta", "M", "2003-07-30",
                    "CPLGCM03L30A271T", "Via A. Maggini", 142,
                    "Ancona", "AN", 60127)
    print(f"{utente.__str__()} {utente.get_eta()}, {utente.get_id()}")

    allenatore = Allenatore("Danny", "Lazzarin", "M", "1986-01-01")
    print(f"{allenatore.__str__()} {allenatore.get_eta()}, {allenatore.get_id()}")

main()