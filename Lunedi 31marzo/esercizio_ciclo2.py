""" chiedi all'utente di inserire un numero e il programma controlla se è un numero pari o no 
se il numero è primo allora lo salva e lo stampa  """

numeri=0
while numeri<=5:
    n=int(input("inserire un numero: "))
    for i in range (n):
        if n<=1:
            print("il numero non è primo")
        else:
            primo=True
            # ciclo verifica se il numero n possiede divisori 
            # tra 2 e la radice di n. in caso ci fosse un divisore significa che n 
            #non è un primo 
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    primo = False
            
