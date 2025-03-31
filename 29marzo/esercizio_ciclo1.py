#esercizio 1 range : conto alla rovescia a partire da un numero dato in input 

#utente inserisce il numero 
controller = True
while controller:
    contatore=int(input("inserire un numero: "))
# conto alla rovescia:
# start=contatore
# stop=-1
    for i in range(contatore,-1,-1):
        print(i)

# chiedere all'utenete se vuole continuare 

    scelta=input("vuoi continuare con le operazioni (si/no): ")
    if scelta=="no":
        controller = False

