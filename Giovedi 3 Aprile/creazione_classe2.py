
# Esercizio 2
""" Crea una classe chiamata Libro. Questa classe dovrebbe avere:

Tre attributi: titolo, autore e pagine.

Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine """

class Libro:  # Dichiaro la classe
    
    def __init__(self, titolo, autore, pagine):  # Metodo costruttore per inizializzare l'oggetto
        self.titolo = titolo  # Attributo di istanza 
        self.autore = autore  # Attributo di istanza  
        self.pagine = pagine  # Attributo di istanza 
    
    def descrizione(self):  # descrizione' -> restituisca una stringa
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine")
        
Libro1 = Libro("Il grande Gatsby", "F. Scott Fitzgerald", 500)  # Crea un oggetto di Libro
Libro2 = Libro("1984", "George Orwell", 328)   # Crea un altro oggetto di Libro

Libro1.descrizione() # Il libro Il grande Gatsby è stato scritto da F. Scott Fitzgerald e ha 500 pagine
Libro2.descrizione() # Stampa Il libro 1984 è stato scritto da George Orwell e ha 328 pagine
