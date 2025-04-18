
import random

def genera_isbn():
    cifre=random.sample("0123456789",10)
    return ''.join(cifre)


class Libri():
    
    catalogo={}
    #costruttore 
    def __init__(self):
        self.titolo=input("Inserisci nome del libro: ")
        self.autore=input("Inserisci nome e cognome dell'autore: ")
        self.isbn=genera_isbn()
        self.catalogo[self.titolo]=(self.autore,self.isbn)
    #metodo deve restituire una stringa 
    def descrizione(self):
        print(f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}")
        
        

