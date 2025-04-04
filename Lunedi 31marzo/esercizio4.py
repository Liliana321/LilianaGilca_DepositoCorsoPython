""" esercizio 1: Scrivi un sistema che prende in input un numero e stampa "Pari" 
se il numero è pari e "Dispari" se il numero è dispari. """

""" """ 
# input numero 
num=int(input("inserire il numero:"))

# se il numero diviso 2 ha resto 0 -> pari 
# altrimenti -> dispari  

if num%2==0:
    print(f"il numero {num} è pari ")
else:
    print(f"il numero {num} è dispari ")


 
"""  esercizio 2: Scrivi un sistema che prende in input un numero intero 
 positivo n e stampa tutti i numeri da n a 0 (compreso), 
 decrementando di 1. Deve potersi ripetere all'infinito. """

""" 
"""
#condizione booleana 
controller = True


while controller:
    num=int(input("inserire un numero: "))
    if num>0:
# conto alla rovescia:
# start=contatore
# stop=-1
        for i in range(num,-1,-1):
            print(i)
    else:
        print("inserisci un numero positivo")



'''esercizio 3: Scrivi un sistema che prende in input una 
lista di numeri e stampa il quadrato di ciascun 
numero nella lista. '''


# input numero degli elementi lista 
element=int(input("inserisci un numero: "))
conteggio=0
lista=[]
# inserisco da tastiera ciascun elemento 
while conteggio<element:
    num=int(input("inserisci numero: "))
    lista.append(num)
    conteggio +=1 
# per ogni valore stampo il quadrato   
for i in lista:
    print(i**2)
    