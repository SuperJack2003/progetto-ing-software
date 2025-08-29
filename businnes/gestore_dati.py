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

cartella_progetto = Path(__file__).parent.resolve()
cartella_dati = Path(cartella_progetto / 'data')
cartella_dati.mkdir(parents=True, exist_ok=True)

file_utenti = cartella_dati / 'utenti.pkl'
file_abbonamenti = cartella_dati / 'abbonamenti.pkl'
file_corsi = cartella_dati / 'corsi.pkl'
file_schede = cartella_dati / 'schede.pkl'
file_esercizi = cartella_dati / 'esercizi.pkl'
file_contratti = cartella_dati / 'contratti.pkl'
file_notifiche = cartella_dati / 'notifiche.pkl'
file_contatori = cartella_dati / 'contatori.pkl'

def carica_dati(gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori, gestore_abbonamenti: GestoreAbbonamenti,
                gestore_corsi: GestoreCorsi, gestore_schede: GestoreSchede, gestore_notifiche: GestoreNotifiche):
    try:
        with open(file_utenti, 'rb') as f:
            print ("Caricamento utenti...")

            lista_utenti = pickle.load(f)
            lista_atleti = lista_utenti["atleti"]
            lista_allenatori = lista_utenti["allenatori"]

            #Caricamento Utenti
            gestore_atleti.set_lista_atleti(lista_atleti)
            gestore_allenatori.set_lista_allenatori(lista_allenatori)

    except FileNotFoundError:
        print(f"File {file_utenti} non trovato")

    except EOFError:
        print(f"File {file_utenti} vuoto")

    try:
        with open(file_abbonamenti, 'rb') as f:
            print ("Caricamento abbonamenti...")

            lista_abbonamenti = pickle.load(f)

            #Caricamento Abbonamenti
            gestore_abbonamenti.set_lista_abbonamenti(lista_abbonamenti)

    except FileNotFoundError:
        print(f"File {file_abbonamenti} non trovato")

    except EOFError:
        print(f"File {file_abbonamenti} vuoto")

    try:
        with open(file_corsi, 'rb') as f:
            print ("Caricamento corsi...")

            lista_corsi = pickle.load(f)

            #Caricamento Corsi
            gestore_corsi.set_lista_corsi(lista_corsi)

    except FileNotFoundError:
        print(f"File {file_corsi} non trovato")

    except EOFError:
        print(f"File {file_corsi} vuoto")

    try:
        with open(file_schede, 'rb') as f:
            print ("Caricamento schede...")

            lista_schede = pickle.load(f)

            #Caricamento Schede
            gestore_schede.set_lista_schede(lista_schede)

    except FileNotFoundError:
        print(f"File {file_schede} non trovato")

    except EOFError:
        print(f"File {file_schede} vuoto")

    try:
        with open(file_esercizi, 'rb') as f:
            print ("Caricamento esercizi...")

            lista_esercizi = pickle.load(f)

            #Caricamento Esercizi
            gestore_schede.set_lista_esercizi(lista_esercizi)

    except FileNotFoundError:
        print(f"File {file_esercizi} non trovato")

    except EOFError:
        print(f"File {file_esercizi} vuoto")

    try:
        with open(file_contratti, 'rb') as f:
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

    except FileNotFoundError:
        print(f"File {file_contratti} non trovato")

    except EOFError:
        print(f"File {file_contratti} vuoto")

    try:
        with open(file_notifiche, 'rb') as f:
            print ("Caricamento notifiche...")

            lista_notifiche = pickle.load(f)

            #Caricamento Notifiche
            gestore_notifiche.set_lista_notifiche(lista_notifiche)

    except FileNotFoundError:
        print(f"File {file_notifiche} non trovato")

    except EOFError:
        print(f"File {file_notifiche} vuoto")

    try:
        with open(file_contatori, "rb") as f:
            contatori = pickle.load(f)
            Contratto.set_last_id(contatori["contatore_contratti"])
            Utente.set_last_id(contatori["contatore_utenti"])
            Abbonamento.set_last_id(contatori["contatore_abbonamenti"])
            Corso.set_last_id(contatori["contatore_corsi"])
            Esercizio.set_last_id(contatori["contatore_esercizi"])
            Notifica.set_last_id(contatori["contatore_notifiche"])
            Scheda.set_last_id(contatori["contatore_schede"])

    except FileNotFoundError:
        print(f"File {file_contatori} non trovato")

    except EOFError:
        print(f"File {file_contatori} vuoto")

def salva_dati(gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori, gestore_abbonamenti: GestoreAbbonamenti,
                gestore_corsi: GestoreCorsi, gestore_schede: GestoreSchede, gestore_notifiche: GestoreNotifiche):

    try:
        with open(file_utenti, 'wb') as f:
            print ("Salvataggio utenti...")

            lista_atleti = gestore_atleti.get_lista_atleti()
            lista_allenatori = gestore_allenatori.get_lista_allenatori()

            lista_utenti = {
                "atleti": lista_atleti,
                "allenatori": lista_allenatori,
            }

            pickle.dump(lista_utenti, f)

    except FileNotFoundError:
        print(f"File {file_utenti} non trovato")

    except EOFError:
        print(f"File {file_utenti} vuoto")

    try:
        with open(file_abbonamenti, 'wb') as f:
            print ("Salvataggio abbonamenti...")

            lista_abbonamenti = gestore_abbonamenti.get_lista_abbonamenti()
            pickle.dump(lista_abbonamenti, f)

    except FileNotFoundError:
        print(f"File {file_abbonamenti} non trovato")

    except EOFError:
        print(f"File {file_abbonamenti} vuoto")

    try:
        with open(file_corsi, 'wb') as f:
            print ("Salvataggio corsi...")

            lista_corsi = gestore_corsi.get_lista_corsi()
            pickle.dump(lista_corsi, f)

    except FileNotFoundError:
        print(f"File {file_corsi} non trovato")

    except EOFError:
        print(f"File {file_corsi} vuoto")

    try:
        with open(file_schede, 'wb') as f:
            print ("Salvataggio schede...")

            lista_schede = gestore_schede.get_lista_schede()
            pickle.dump(lista_schede, f)

    except FileNotFoundError:
        print(f"File {file_schede} non trovato")

    except EOFError:
        print(f"File {file_schede} vuoto")

    try:
        with open(file_esercizi, 'wb') as f:
            print ("Salvataggio esercizi...")

            lista_esercizi = gestore_schede.get_lista_esercizi()
            pickle.dump(lista_esercizi, f)

    except FileNotFoundError:
        print(f"File {file_esercizi} non trovato")

    except EOFError:
        print(f"File {file_esercizi} vuoto")

    try:
        with open(file_contratti, 'wb') as f:
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

    except FileNotFoundError:
        print(f"File {file_contratti} non trovato")

    except EOFError:
        print(f"File {file_contratti} vuoto")

    try:
        with open(file_notifiche, 'wb') as f:
            print("Salvataggio notifiche...")

            lista_notifiche = gestore_notifiche.get_lista_notifiche()
            pickle.dump(lista_notifiche, f)

    except FileNotFoundError:
        print(f"File {file_notifiche} non trovato")

    except EOFError:
        print(f"File {file_notifiche} vuoto")

    try:
        with open(file_contatori, "wb") as f:
            contatore_contratti = Contratto.get_last_id()
            contatore_utenti = Utente.get_last_id()
            contatore_abbonamenti = Abbonamento.get_last_id()
            contatore_corsi = Corso.get_last_id()
            contatore_esercizi = Esercizio.get_last_id()
            contatore_notifiche = Notifica.get_last_id()
            contatore_schede = Scheda.get_last_id()

            contatori = {
                "contatore_contratti": contatore_contratti,
                "contatore_utenti": contatore_utenti,
                "contatore_abbonamenti": contatore_abbonamenti,
                "contatore_corsi": contatore_corsi,
                "contatore_esercizi": contatore_esercizi,
                "contatore_notifiche": contatore_notifiche,
                "contatore_schede": contatore_schede,
            }

            pickle.dump(contatori, f)

    except FileNotFoundError:
        print(f"File {file_contatori} non trovato")

    except EOFError:
        print(f"File {file_contatori} vuoto")

def elimina_dati():
    nomi_file_dati = [
        'utenti.pkl',
        'abbonamenti.pkl',
        'corsi.pkl',
        'schede.pkl',
        'esercizi.pkl',
        'contratti.pkl',
        'notifiche.pkl',
    ]

    for nome_file in nomi_file_dati:
        percorso = cartella_dati / nome_file

        try:
            with open(percorso, "wb") as f:
                continue
        except Exception as e:
            print (f"Errore durante la scrittura del file: {e}")

    try:
        with open(file_contatori, "wb") as f:
            contatori = {
                "contatore_contratti": 0,
                "contatore_utenti": 0,
                "contatore_abbonamenti": 0,
                "contatore_corsi": 0,
                "contatore_esercizi": 0,
                "contatore_notifiche": 0,
                "contatore_schede": 0,
            }

            pickle.dump(contatori, f)

    except Exception as e:
        print(f"Errore durante la scrittura del file: {e}")