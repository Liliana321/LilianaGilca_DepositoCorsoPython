""" Base / Numeri pari e dispari o sequenza

Descrizione: Scrivi un programma che chiede all'utente di inserire 
un numero o una stringa scegliendo prima quale. Il programma 
dovrebbe determinare se il numero è pari o dispari e stampare il risultato e se deve ripetere 
o stampare e poi ripetere. """

scelta=input("inserire una scelta: (digitare 'n' per numeri o 's' per stringa):")
contatore=True
while contatore:
    match scelta:
        case "s":
            stringa=input("inserisci a tuo piacere una stringa:")
            if len(stringa)%2==0:
                print("la stringa contiene elementi pari ")
            else:
                print(f"la stringa contiene elementi dispari, ovvero {len(stringa)} char")
        case "n":
            numero=int(input("inserisci a tuo piacere un numero:"))
            if numero%2==0:
                print(f"il numero {numero} è pari ")
            else:
                print(f"il numero {numero} è dispari ")
        case _:
            print("error")
            
    rip=input("vuoi ripetere l'operazione: ")
    if rip=="no":
        break
    
    
    
""" Chiedi all'utente di inserire due numeri che definiscono un intervallo 
(es. 10 e 50). Il programma dovrebbe stampare tutti i numeri 
primi compresi in quell'intervallo o i numeri non primi o entrambi 
divisi a tua scelta,
salvandoli in due aggregazioni differenti e chiedere se deve ripetere. """

while True:
    a = int(input("Inserisci un primo numero: "))
    b = int(input(f"Inserisci un secondo numero più grande di {a}: "))

    numeri = [*range(a, b)]
    print(numeri)

    numeri_primi = []
    numeri_nonprimi = []

    # Iteriamo attraverso la lista di numeri e verifichiamo se sono primi
    for n in numeri:
        primo = True  #N primo
        if n > 1:  
            for i in range(2, int(n**0.5) + 1):  
                if n % i == 0:
                    primo = False
                    break  # Interrompi il ciclo se il numero non è primo
            if primo:  # Se il numero è primo
                numeri_primi.append(n)
            else:
                numeri_nonprimi.append(n)
        else:
            numeri_nonprimi.append(n)


    print("1. Stampare numeri primi")
    print("2. Stampare numeri non primi")
    print("3. Stampare entrambi ")

    scelta = int(input("Scegliere tra le 3 opzioni: "))

    match scelta:
        case 1:
            print("I numeri primi risultano:", numeri_primi)
        case 2:
            print("I numeri non primi risultano:", numeri_nonprimi)
        case 3:
            print("I numeri primi risultano:", numeri_primi)
            print("I numeri non primi risultano:", numeri_nonprimi)

