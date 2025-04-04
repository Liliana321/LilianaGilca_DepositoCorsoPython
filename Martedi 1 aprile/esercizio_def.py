
import random

def indovina():
    a=random.randint(1,100)
    
    tentativo=None
    
    print("Benvenuto al gioco! Indovina il numero tra 1 e 100:")

    while tentativo!= a:
        tentativo=int(input("inserisci un numero da 0 a 100:"))
        
        #condizioni 
        if tentativo < a:
            print("Il numero è più alto!")
        elif tentativo > a:
            print("Il numero è più basso!")
    
    print("Hai indovinato il numero!")

# Esegui il gioco
indovina()
        