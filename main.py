from domain.attività.allenatore import Allenatore
from domain.attività.atleta import Atleta

def main():


    allenatore = Allenatore("Danny", "Lazzarin", "M", "1986-01-01", "CDCFSL1", "Via Cavour", 10,
                            "Padova", "PV", 1, "telefono_danny", "email_danny")
    print(f"{allenatore.__str__()} {allenatore.get_eta()}, {allenatore.get_id()}")

main()