from persona import Persona
from derivate_persona import Studente,Professore
def menu():
    studenti = {}  # Dizionario con nome come chiave e oggetto Studente come valore
    professore = None

    while True:
        print("\n--- MENU ---")
        print("1. Crea uno Studente")
        print("2. Crea un Professore")
        print("3. Mostra tutti gli studenti")
        print("4. Presentazione di uno Studente")
        print("5. Calcola media di uno Studente")
        print("6. Presentazione Professore")
        print("7. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                nome = input("Nome dello studente: ")
                eta = int(input("Età dello studente: "))
                voti_input = input("Inserisci i voti separati da virgola: ")
                voti = [int(v) for v in voti_input.split(",")]
                studenti[nome] = Studente(nome, eta, voti)
                print(f"Studente '{nome}' creato con successo.")

            case "2":
                nome = input("Nome del professore: ")
                eta = int(input("Età del professore: "))
                materia = input("Materia insegnata: ")
                professore = Professore(nome, eta, materia)
                print("Professore creato con successo.")

            case "3":
                if studenti:
                    print("Studenti disponibili:")
                    for nome in studenti:
                        print(f"- {nome}")
                else:
                    print("Nessuno studente ancora creato.")

            case "4":
                nome = input("Inserisci il nome dello studente: ")
                studente = studenti.get(nome)
                if studente:
                    print(studente.presentazione())
                else:
                    print("Studente non trovato.")

            case "5":
                nome = input("Inserisci il nome dello studente: ")
                studente = studenti.get(nome)
                if studente:
                    media = studente.calcola_media()
                    print(f"La media dei voti di {nome} è {media:.2f}")
                else:
                    print("Studente non trovato.")

            case "6":
                if professore:
                    print(professore.presentazione())
                else:
                    print("Nessun professore ancora creato.")

            case "7":
                print("Uscita dal programma...")
                break

            case _:
                print("Scelta non valida. Riprova.")

# Avvio del programma
menu()