#extra

scelta= int(input("inserisci scelta esercizio (1/2/3): "))

match scelta:
    case 1:
        num=int(input("inserire il numero:"))

# se il numero diviso 2 ha resto 0 -> pari 
# altrimenti -> dispari  

        if num%2==0:
            print(f"il numero {num} è pari ")
        else:
             print(f"il numero {num} è dispari ")
    case 2:
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
    case 3:
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




    