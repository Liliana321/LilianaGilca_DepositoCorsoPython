
import Classe_libro as libro

libri = libro.Libri()

class Libreria():
    
    def __init__(self):
        self.catalogo=libri.catalogo

    
    def aggiungi_libro(self):
        self.titolo=input("Inserisci nome del libro: ")
        self.autore=input("Inserisci nome e cognome dell'autore: ")
        self.isbn=libro.genera_isbn()
        
        self.catalogo[self.titolo]=(self.autore,self.isbn)
    
    def rimuovi_libro(self):
        isbn_rimoz=int(input("Inserisci ISBN del libro da rimuovere. "))
        
        scelta=input("Sei sicuro di procedere con la rimozione? (s/n): ").lower()
        match scelta:
            case "si":
                libro_trovato=False
                for titolo,(autore,isbn) in list(self.catalogo.items()):
                    if isbn==isbn_rimoz:
                        del self.catalogo[titolo]
                        print(f"Il libro '{titolo}' è stato rimosso dal catalogo.")
                        libro_trovato = True
                        break
                if not libro_trovato:
                    print("Nessun libro trovato con l'ISBN inserito.")
                    
            case _:
                print("Grazie per la scelta!")
                
    def cerca_per_titolo(self):
        title=input("Inserisci titolo per la ricerca: ")
        for titolo,(autore,isbn) in list(self.catalogo.items()):
            if title==titolo:
                print(f"Titolo: {titolo}, Autore: {autore}, ISBN: {isbn}")
                return
        print("Titolo non trovato. Ci dispiace!")
        
    def mostra_catalogo(self):
        for titolo,(autore,isbn) in list(self.catalogo.items()):
                print(f"Titolo: {titolo}, Autore: {autore}, ISBN: {isbn}")
            
    
        
        
    
               
               
                        
        
        
        