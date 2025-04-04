
class Biblioteca:  # Dichiaro la classe
    
    def __init__(self, titolo):  # Metodo costruttore per inizializzare l'oggetto
        self.titolo = titolo  # Attributo di istanza 

    
    def creazione(self):  # dcreazione -> restituisca una stringa
        print(f"Il libro {self.titolo} è stato creato.")
  
 
titolo_libro=input("Inserisci Titolo: ")
libro_singolo = Biblioteca(titolo_libro)
libro_singolo.creazione() 


contatore=1 # Un libro è stato già creato
n=int(input("Quanti Libri vuoi creare? ") ) 
libri = [libro_singolo]

# Ciclo while per creare n libri 
while contatore < n:
    titolo = input(f"Inserisci il titolo del libro {contatore+1}: ") 
    libro = Biblioteca(titolo)  # Crea l'oggetto 
    libro.creazione() 
    libri.append(libro)  # Aggiunge l'oggetto alla lista
    contatore += 1 

# Mostra i libri creati
#print(libri)
print("Libri creati:")
for libro in libri:
    print(libro.titolo)
    
#Il grande Gatsby
#1984
#Il Signore degli Anelli
