from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori
from businnes.gestore_abbonamenti import GestoreAbbonamenti
from businnes.gestore_corsi import GestoreCorsi
from businnes.gestore_schede import GestoreSchede
from businnes.gestore_notifiche import GestoreNotifiche
import businnes.gestore_dati as dati

def main():
    dati.elimina_dati()

    gestore_atleti = GestoreAtleti()
    gestore_allenatori = GestoreAllenatori()
    gestore_abbonamenti = GestoreAbbonamenti()
    gestore_corsi = GestoreCorsi()
    gestore_schede = GestoreSchede()
    gestore_notifiche = GestoreNotifiche()

    gestore_allenatori.set_gestori(gestore_atleti)
    gestore_abbonamenti.set_gestori(gestore_atleti)
    gestore_corsi.set_gestori(gestore_atleti, gestore_allenatori)
    gestore_schede.set_gestori(gestore_atleti, gestore_allenatori, gestore_abbonamenti)
    gestore_notifiche.set_gestori(gestore_atleti, gestore_allenatori)

    dati.carica_dati(gestore_atleti, gestore_allenatori, gestore_abbonamenti, gestore_corsi, gestore_schede, gestore_notifiche)

    gestore_atleti.aggiungi_atleta("Giacomo", "Cipolletta", "M", "2003-07-30", "CPLGCM03L30A271T")
    gestore_allenatori.aggiungi_allenatore("Denny", "Lazzarin", "M", "1981-01-01", "CFDENNY")

    for allenatore in gestore_allenatori.get_lista_allenatori():
        print(f"\nAllenatore: {allenatore.__str__()} id: {allenatore.get_id()}")

    print("\n")

    gestore_allenatori.aggiungi_contratto(2, 1)
    i = 1

    for contratto in gestore_allenatori.get_lista_contratti():
        atleta = gestore_atleti.get_atleta_per_id(contratto.get_atleta())
        allenatore = gestore_allenatori.get_allenatore_per_id(contratto.get_allenatore())
        print(f"\nContratto n.{i}: Atleta: {atleta.__str__()}, Allenatore: {allenatore.__str__()}")

    print("\n")

    gestore_abbonamenti.crea_abbonamento(1, "corsi+sala")
    gestore_abbonamenti.crea_abbonamento(1, "corsi")

    gestore_abbonamenti.crea_contratto(1, 1)
    i = 1
    for contratto in gestore_abbonamenti.get_lista_contratti():
        atleta = gestore_atleti.get_atleta_per_id(contratto.get_atleta())
        abbonamento = gestore_abbonamenti.get_abbonamento(contratto.get_abbonamento())
        print(f"\nContratto n.{i}: Atleta: {atleta.__str__()}, Abbonamento: {abbonamento.get_nome()}. In scadenza il: {contratto.get_scadenza().__str__()}")

    dati.salva_dati(gestore_atleti, gestore_allenatori, gestore_abbonamenti, gestore_corsi, gestore_schede, gestore_notifiche)


main()