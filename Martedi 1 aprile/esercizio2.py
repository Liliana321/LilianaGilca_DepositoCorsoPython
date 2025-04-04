#esercizio completo 

import random

conteggio=True
#ciclo while continua finchè l'utente non inserisce un numero positivo 

while conteggio:
    a=int(input("inserisci un numero:"))
    if a <0 or a==0:
        continue
    else:
        break

print(a)
        
