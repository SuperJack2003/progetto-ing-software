from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori
from businnes.gestore_abbonamenti import GestoreAbbonamenti
from businnes.gestore_corsi import GestoreCorsi
from businnes.gestore_schede import GestoreSchede
from businnes.gestore_notifiche import GestoreNotifiche
import businnes.gestore_dati as dati
from domain.attività.contratto import Contratto
from domain.attività.utente import Utente

from domain.servizio.abbonamento import Abbonamento
from domain.servizio.corso import Corso
from domain.servizio.esercizio import Esercizio
from domain.servizio.notifica import Notifica
from domain.servizio.scheda import Scheda


def main():

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

    view_status(gestore_atleti, gestore_allenatori, gestore_abbonamenti, gestore_corsi, gestore_schede,
                gestore_notifiche)

    dati.salva_dati(gestore_atleti, gestore_allenatori, gestore_abbonamenti, gestore_corsi, gestore_schede, gestore_notifiche)

def view_status(gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori, gestore_abbonamenti: GestoreAbbonamenti,
           gestore_corsi: GestoreCorsi, gestore_schede: GestoreSchede, gestore_notifiche: GestoreNotifiche):

    contatore_contratti = Contratto.get_last_id()
    contatore_utenti = Utente.get_last_id()
    contatore_abbonamenti = Abbonamento.get_last_id()
    contatore_corsi = Corso.get_last_id()
    contatore_esercizi = Esercizio.get_last_id()
    contatore_notifiche = Notifica.get_last_id()
    contatore_schede = Scheda.get_last_id()

    print(f"\n\nNumero utenti: {contatore_utenti}")
    for atleta in gestore_atleti.get_lista_atleti():
        print(f"Atleta n. {atleta.get_id()}: {atleta.__str__()}")
    for allenatore in gestore_allenatori.get_lista_allenatori():
        print(f"Allenatore n. {allenatore.get_id()}: {allenatore.__str__()}")

    print(f"\n\nNumero abbonamenti: {contatore_abbonamenti}")
    for abbonamento in gestore_abbonamenti.get_lista_abbonamenti():
        print(f"Abbonamento n. {abbonamento.get_id()}: {abbonamento.get_nome()}")

    print(f"\n\nNumero_corsi: {contatore_corsi}")
    for corso in gestore_corsi.get_lista_corsi():
        print(f"Corso n. {corso.get_id()}: {corso.get_nome()}")

    print(f"\n\nNumero schede: {contatore_schede}")
    for scheda in gestore_schede.get_lista_schede():
        print(f"Schede n. {scheda.get_id()}, id allenatore: {scheda.get_id_allenatore()}")

    print(f"\n\nNumero esercizi: {contatore_esercizi}")
    for esercizio in gestore_schede.get_lista_esercizi():
        print(f"Esercizio n. {esercizio.get_id()}: {esercizio.get_nome()}")

    print(f"\n\nNumero notifica: {contatore_notifiche}")
    for atleta in gestore_atleti.get_lista_atleti():
        notifiche_atleta = gestore_notifiche.get_notifiche_da_utente(atleta.get_id())
        if notifiche_atleta is not None:
            for notifica in notifiche_atleta:
                print(f"Notifica n. {notifica.get_id()}: {notifica.get_nome()}")

    print(f"\n\nNumero contratti: {contatore_contratti}")

    for contratto_atleta_allenatore in gestore_allenatori.get_lista_contratti():
        atleta = gestore_atleti.get_atleta_per_id(contratto_atleta_allenatore.get_atleta())
        allenatore = gestore_allenatori.get_allenatore_per_id(contratto_atleta_allenatore.get_allenatore())
        print(f"Contratto atleta-allenatore n. {contratto_atleta_allenatore.get_id()}: {atleta.__str__()} - {allenatore.__str__()}")

    for contratto_abbonamento in gestore_abbonamenti.get_lista_contratti():
        atleta = gestore_atleti.get_atleta_per_id(contratto_abbonamento.get_atleta())
        abbonamento = gestore_abbonamenti.get_abbonamento(contratto_abbonamento.get_abbonamento())
        print(f"Contratto abbonamento n. {contratto_abbonamento.get_id()}: {atleta.__str__()} - {abbonamento.get_nome()}")

    for contratto_allenatore_corso in gestore_corsi.get_lista_contratti_allenatori():
        allenatore = gestore_allenatori.get_allenatore_per_id(contratto_allenatore_corso.get_allenatore())
        corso = gestore_corsi.get_corso(contratto_allenatore_corso.get_corso())
        print(f"Contratto allenatore-corso n. {contratto_allenatore_corso.get_id()}: {corso.get_nome()} - {allenatore.__str__()}")

    for contratto_atleta_corso in gestore_corsi.get_lista_contratti_atleti():
        atleta = gestore_atleti.get_atleta_per_id(contratto_atleta_corso.get_atleta())
        corso = gestore_corsi.get_corso(contratto_atleta_corso.get_corso())
        print(f"Contratto atleta-corso n. {contratto_atleta_corso.get_id()}: {corso.get_nome()} - {atleta.__str__()}")

    for contratto_scheda in gestore_schede.get_lista_contratti_schede():
        atleta = gestore_atleti.get_atleta_per_id(contratto_scheda.get_atleta())
        scheda = gestore_schede.get_scheda(contratto_scheda.get_scheda())
        print(f"Contratto scheda n. {contratto_scheda.get_id()}: {scheda.get_id()} - {atleta.__str__()}")

    for contratto_esercizio in gestore_schede.get_lista_contratti_esercizi():
        scheda = gestore_schede.get_scheda(contratto_esercizio.get_scheda())
        esercizio = gestore_schede.get_esercizio(contratto_esercizio.get_esercizio())
        print(f"Contratto esercizio n. {contratto_esercizio.get_id()}: {scheda.get_id()} - {esercizio.get_nome()}")

    print("\n")

main()