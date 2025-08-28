import pickle
from pathlib import Path

from domain.attività.atleta import Atleta
from domain.attività.allenatore import Allenatore
from domain.attività.utente import Utente

from domain.servizio.abbonamento import Abbonamento
from domain.servizio.corso import Corso
from domain.servizio.scheda import Scheda
from domain.servizio.esercizio import Esercizio
from domain.servizio.notifica import Notifica

from domain.attività.contratto import Contratto
from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso
from domain.attività.contratto_scheda import ContrattoScheda
from domain.attività.contratto_esercizio import ContrattoEsercizio
from domain.attività.contratto_abbonamento import ContrattoAbbonamento
from domain.attività.contratto_atleta_allenatore import ContrattoAtletaAllenatore
from domain.attività.contratto_allenatore_corso import ContrattoAllenatoreCorso

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori
from businnes.gestore_corsi import GestoreCorsi
from businnes.gestore_abbonamenti import GestoreAbbonamenti
from businnes.gestore_schede import GestoreSchede
from businnes.gestore_notifiche import GestoreNotifiche

cartella_dati = Path(__file__).parent.parent / 'data'
cartella_dati.mkdir(parents=True, exist_ok=True)

def carica_dati(gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori, gestore_abbonamenti: GestoreAbbonamenti,
                gestore_corsi: GestoreCorsi, gestore_schede: GestoreSchede, gestore_notifiche: GestoreNotifiche):
    try:
        with open(cartella_dati / 'utenti.pkl', 'rb') as f:
            print ("Caricamento utenti...")

            lista_utenti = pickle.load(f)
            lista_atleti = lista_utenti["atleti"]
            lista_allenatori = lista_utenti["allenatori"]

            #Caricamento Utenti
            gestore_atleti.set_lista_atleti(lista_atleti)
            gestore_allenatori.set_lista_allenatori(lista_allenatori)

        with open(cartella_dati / 'abbonamenti.pkl', 'rb') as f:
            print ("Caricamento abbonamenti...")

            lista_abbonamenti = pickle.load(f)

            #Caricamento Abbonamenti
            gestore_abbonamenti.set_lista_abbonamenti(lista_abbonamenti)

        with open(cartella_dati / 'corsi.pkl', 'rb') as f:
            print ("Caricamento corsi...")

            lista_corsi = pickle.load(f)

            #Caricamento Corsi
            gestore_corsi.set_lista_corsi(lista_corsi)

        with open(cartella_dati / 'schede.pkl', 'rb') as f:
            print ("Caricamento schede...")

            lista_schede = pickle.load(f)

            #Caricamento Schede
            gestore_schede.set_lista_schede(lista_schede)

        with open(cartella_dati / 'esercizi.pkl', 'rb') as f:
            print ("Caricamento esercizi...")

            lista_esercizi = pickle.load(f)

            #Caricamento Esercizi
            gestore_schede.set_lista_esercizi(lista_esercizi)

        with open(cartella_dati / 'contratti.pkl', 'rb') as f:
            print("Caricamento contratti...")

            lista_contratti = pickle.load(f)
            lista_contratti_abbonamento = lista_contratti["contratti_abbonamento"]
            lista_contratti_scheda = lista_contratti["contratti_scheda"]
            lista_contratti_esercizi = lista_contratti["contratti_esercizi"]
            lista_contratti_allenatore_corso = lista_contratti["contratti_allenatore_corso"]
            lista_contratti_atleta_corso = lista_contratti["contratti_atleta_corso"]
            lista_contratti_allenatore_atleta = lista_contratti["contratti_allenatore_atleta"]

            #Caricamento Contratti Allenatori
            gestore_allenatori.set_lista_contratti(lista_contratti_allenatore_atleta)

            #Caricamento Contratti Abbonamenti
            gestore_abbonamenti.set_lista_contratti(lista_contratti_abbonamento)

            #Caricamento Contratti Corsi
            gestore_corsi.set_lista_contratti_allenatori(lista_contratti_allenatore_corso)
            gestore_corsi.set_lista_contratti_atleti(lista_contratti_atleta_corso)

            #Caricamento Contratti Scede
            gestore_schede.set_lista_contratti_esercizi(lista_contratti_esercizi)
            gestore_schede.set_lista_contratti_schede(lista_contratti_scheda)

        with open(cartella_dati / 'notifiche.pkl', 'wb') as f:
            print ("Caricamento notifiche...")

            lista_notifiche = pickle.load(f)

            #Caricamento Notifiche
            gestore_notifiche.set_lista_notifiche(lista_notifiche)

    except FileNotFoundError:
        print(f"File {f} non trovato")

def salva_dati(gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori, gestore_abbonamenti: GestoreAbbonamenti,
                gestore_corsi: GestoreCorsi, gestore_schede: GestoreSchede, gestore_notifiche: GestoreNotifiche):

    try:
        with open(cartella_dati / 'utenti.pkl', 'wb') as f:
            print ("Salvataggio utenti...")

            lista_atleti = gestore_atleti.get_lista_atleti()
            lista_allenatori = gestore_allenatori.get_lista_allenatori()

            lista_utenti = {
                "atleti": lista_atleti,
                "allenatori": lista_allenatori,
            }

            pickle.dump(lista_utenti, f)

        with open(cartella_dati / 'abbonamenti.pkl', 'wb') as f:
            print ("Salvataggio abbonamenti...")

            lista_abbonamenti = gestore_abbonamenti.get_lista_abbonamenti()
            pickle.dump(lista_abbonamenti, f)

        with open(cartella_dati / 'corsi.pkl', 'wb') as f:
            print ("Salvataggio corsi...")

            lista_corsi = gestore_corsi.get_lista_corsi()
            pickle.dump(lista_corsi, f)

        with open(cartella_dati / 'schede.pkl', 'wb') as f:
            print ("Salvataggio schede...")

            lista_schede = gestore_schede.get_lista_schede()
            pickle.dump(lista_schede, f)

        with open(cartella_dati / 'esercizi.pkl', 'wb') as f:
            print ("Salvataggio esercizi...")

            lista_esercizi = gestore_schede.get_lista_esercizi()
            pickle.dump(lista_esercizi, f)

        with open(cartella_dati / 'contratti.pkl', 'wb') as f:
            print ("Salvataggio contratti...")

            lista_contratti_abbonamento = gestore_abbonamenti.get_lista_contratti()
            lista_contratti_scheda = gestore_schede.get_lista_contratti_schede()
            lista_contratti_esercizi = gestore_schede.get_lista_contratti_esercizi()
            lista_contratti_allenatore_corso = gestore_corsi.get_lista_contratti_allenatori()
            lista_contratti_atleta_corso = gestore_corsi.get_lista_contratti_atleti()
            lista_contratti_allenatore_atleta = gestore_allenatori.get_lista_contratti()

            lista_contratti = {
                "contratti_abbonamento": lista_contratti_abbonamento,
                "contratti_scheda": lista_contratti_scheda,
                "contratti_esercizi": lista_contratti_esercizi,
                "contratti_allenatore_corso": lista_contratti_allenatore_corso,
                "contratti_atleta_corso": lista_contratti_atleta_corso,
                "contratti_allenatore_atleta": lista_contratti_allenatore_atleta,
            }

            pickle.dump(lista_contratti, f)

        with open(cartella_dati / 'notifiche.pkl', 'wb') as f:
            print("Salvataggio notifiche...")

            lista_notifiche = gestore_notifiche.get_lista_notifiche()
            pickle.dump(lista_notifiche, f)

    except FileNotFoundError:
        print(f"File {f} non trovato")