# # creazione di una classe

class Automobile:  # Dichiaro la classe
    numero_di_ruote = 4  # Attributo di classe - numero di ruote comune a tutte le istanze

    def __init__(self, marca, modello):  # Metodo costruttore per inizializzare l'oggetto
        self.marca = marca  # Attributo di istanza - marca dell'automobile
        self.modello = modello  # Attributo di istanza - modello dell'automobile

    def stampa_info(self):  # Metodo di istanza per stampare le informazioni sull'automobile
        print("L'automobile è una", self.marca, self.modello)  # Stampa marca e modello

auto1 = Automobile("Fiat", "500")  # Crea un oggetto di Automobile
auto2 = Automobile("BMW", "X3")   # Crea un altro oggetto di Automobile

auto1.stampa_info()  # Stampa "L'automobile è una Fiat 500"
auto2.stampa_info()  # Stampa "L'automobile è una BMW X3"

class Persona:
    def __init__(self, nome, eta):  
        self.nome = nome  # Attributo per memorizzare il nome
        self.eta = eta    # Attributo per memorizzare l'età

# Creazione di un oggetto Persona
p = Persona("Pippo", 30)

print(p.nome)  # Output: Pippo
print(p.eta)   # Output: 30

#MODELLO STATICO
# Esempio di un metodo statico
class Calcolatrice:
    @staticmethod
    def somma(a, b):  # Metodo statico per sommare due numeri
        return a + b

# Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)  


#METODO DI CLASSE 
#Metodo decorato: mostra numero istanze è un metodo di classe 
#si utilizza il decoratore

class Contatore:
    numero_istanze=0 # Attributo di class
        
    def __init__(self):  # Metodo costruttore
        Contatore.numero_istanze += 1  # Ogni volta che viene creata una nuova istanza, incremento il contatore

    @classmethod
    def mostra_numero_istanze(cls):  # Metodo di classe per mostrare il numero di istanze create
        print(f"Sono state create {cls.numero_istanze} istanze.")  # Stampa il numero di istanze create

# Creazione di alcune istanze: conserva l'ultimo elemento salvato 
c1 = Contatore()  # Creazione prima istanza 
c2 = Contatore()  # Creazione seconda istanza

Contatore.mostra_numero_istanze()  # Chiamo il metodo di classe per mostrare il numero di istanze create
# Output: Sono state create 2 istanze.