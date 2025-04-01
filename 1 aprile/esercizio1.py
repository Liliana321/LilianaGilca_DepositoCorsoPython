
""" Esercizio 1  """

""" Scrivi un programma che chiede all'utente di inserire un 
numero intero positivo n. Il programma deve poi eseguire le seguenti 
operazioni:

Utilizzare un ciclo while per garantire che 
l'utente inserisca un numero positivo. Se l'utente inserisce 
un numero negativo o zero,
il programma deve continuare a chiedere un numero fino a 
quando non viene inserito un numero positivo. """

conteggio=True
#ciclo while continua finchè l'utente non inserisce un numero positivo 

while conteggio:
    a=int(input("inserisci un numero:"))
    if a <0 or a==0:
        continue
    else:
        break

print(a)
    
""" Utilizzare un ciclo for con range
per calcolare e stampare la somma dei numeri pari da 1 a n. """

""" Utilizzare un ciclo for per 
stampare tutti i numeri dispari da 1 a n.
Utilizzare una struttura if per determinare se n è un numero primo. Un numero 
primo è divisibile solo per 1 e per se stesso. Il programma deve stampare 
se n è primo o no.


"""


# input n per il range che va da 1 a n 
n=int(input("inserisci un numero n:"))
numeri=[*range(1,n+1)] #n+1 perche il range arriva fino a n-1
num_pari=[]
num_dispari=[]
num_primi=[]


#ciclo che intera su tutti i numeri nella lista numeri 

for i in numeri:
    if i > 1:  # Inizia la verifica da 2 per il controllo primo
        for j in range(2, i): # ciclo per dividere i con ogni numero da 2 a i-1
            if i % j == 0:
                print(f"{i} non è un numero primo")
                break
        else:
            num_primi.append(i)
    
    if i % 2 == 0: #ciclo per numeri pari e dispari 
        num_pari.append(i)
    else:
        num_dispari.append(i)
    
print(sum(num_pari))
print(num_dispari)
print(num_primi)

