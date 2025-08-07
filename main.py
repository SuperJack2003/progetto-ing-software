from domain.entities.allenatore import Allenatore
from domain.entities.atleta import Atleta


def main():
    utente = Atleta("Giacomo", "Cipolletta", "M", "2003-07-30",
                    "CPLGCM03L30A271T", "Via A. Maggini", 142,
                    "Ancona", "AN", 60127)
    print(f"{utente.__str__()} {utente.getEta()}, {utente.getRuolo()}, "
          f"{utente.getIndirizzo().__str__()}")

    allenatore = Allenatore("Danny", "Lazzarin", "M", "1986-01-01")
    print(f"{allenatore.__str__()} {allenatore.getEta()}, {allenatore.getRuolo()}")

main()