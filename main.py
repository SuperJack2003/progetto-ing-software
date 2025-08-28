from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori
from businnes.gestore_abbonamenti import GestoreAbbonamenti
from businnes.gestore_corsi import GestoreCorsi
from businnes.gestore_schede import GestoreSchede
from businnes.gestore_notifiche import GestoreNotifiche
import businnes.gestore_dati as dati

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

    while True:
        print("Dati caricati! Cosa vuoi fare?")
        print("1. Crea Atleta"
              "2. Visualizza Atleti"
              "3. Crea Allenatore"
              "4. Visualizza Allenatori"
              "5. Salva e chiudi")

        choice = input()
        if choice == "1":
            crea_atleta(gestore_atleti)
        elif choice == "2":
            visualizza_atleti(gestore_atleti)
        elif choice == "3":
            crea_allenatore(gestore_allenatori)
        elif choice == "4":
            visualizza_allenatori(gestore_allenatori)
        elif choice == "5":
            dati.salva_dati(gestore_atleti, gestore_allenatori, gestore_abbonamenti, gestore_corsi, gestore_schede, gestore_notifiche)
            print ("Arrivederci")
            break
        else:
            print("Opzione non valida")


def crea_atleta(gestore_atleti: GestoreAtleti):
    print("Inserire i dati in ordine:")

    nome = input ("Nome: ")
    cognome = input ("Cognome: ")
    sesso = input ("Sesso: ")
    nascita = input ("Nascita: ")
    codice_fiscale = input ("Codice fiscale: ")
    via = input ("Via: ")
    civico = int(input ("Civico: "))
    citta = input ("Citta: ")
    provincia = input ("Provincia: ")
    cap = int(input ("Cap: "))
    telefono = input ("Telefono: ")
    email = input ("Email: ")

    risultato = gestore_atleti.aggiungi_atleta(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta, provincia, cap, telefono, email)

    if risultato:
        print("Operazione riuscita con successo")
    else:
        print("Operazione non riuscita")

def visualizza_atleti(gestore_atleti: GestoreAtleti):
    lista_atleti = gestore_atleti.get_lista_atleti()
    i = 0

    for atleta in lista_atleti:
        print(f"{++i}. {atleta.__str__()}")

def crea_allenatore(gestore_allenatori: GestoreAllenatori):
    print("Inserire i dati in ordine:")

    nome = input("Nome: ")
    cognome = input("Cognome: ")
    sesso = input("Sesso: ")
    nascita = input("Nascita: ")
    codice_fiscale = input("Codice fiscale: ")
    via = input("Via: ")
    civico = int(input("Civico: "))
    citta = input("Citta: ")
    provincia = input("Provincia: ")
    cap = int(input("Cap: "))
    telefono = input("Telefono: ")
    email = input("Email: ")

    risultato = gestore_allenatori.aggiungi_allenatore(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta, provincia, cap, telefono, email)

    if risultato:
        print("Operazione riuscita con successo")
    else:
        print("Operazione non riuscita")

def visualizza_allenatori(gestore_allenatori: GestoreAllenatori):
    lista_allenatori = gestore_allenatori.get_lista_allenatori()
    i = 0

    for allenatore in lista_allenatori:
        print(f"{++i}. {allenatore.__str__()}")

main()