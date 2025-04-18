from Classe_libreria import Libreria
from Classe_libro import Libri

libreria = Libreria()

def menu():
    print("\n=== MENU LIBRERIA ===")
    print("1. Aggiungi libro")
    print("2. Rimuovi libro")
    print("3. Cerca libro per titolo")
    print("4. Mostra catalogo")
    print("5. Esci")

def main():
    

    while True:
        menu()
        scelta = input("Scegli un'opzione (1-5): ")

        match scelta:
            case "1":
                libreria.aggiungi_libro()
            case "2":
                libreria.rimuovi_libro()
            case "3":
                libreria.cerca_per_titolo()
            case "4":
                libreria.mostra_catalogo()
            case "5":
                print("Uscita dal programma. A presto!")
                break
            case _:
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
