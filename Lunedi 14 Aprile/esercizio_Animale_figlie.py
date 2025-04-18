# ESERCIZIO 

class Animale():
    def __init__(self,nome,eta):
        self.nome=nome
        self.eta=eta
        
    def informazioni(self):
        self.peso=int(input("Inserisci il peso dell'animale: "))
        self.sesso=input("inserisci sesso (M/F):").upper()
        print(f"{self.nome} ha {self.eta} anni, pesa {self.peso} e di sesso {self.sesso}.")
        
    def fai_suono(self):
        print(f"{self.nome} fa un verso")
        
class Leone(Animale):
    def __init__(self,nome,eta):
        super().__init__(nome,eta)
        
    def fai_suono(self):
        print(f"{self.nome} ruggisce.")
    
    def caccia(self):
        print(f"{self.nome} è un leone e caccia altri animali.")
        
    def informazioni(self):
        return super().informazioni() #richiamo il metodo della classe madre 
        
class Giraffa(Animale):
    def __init__(self,nome,eta):
        super().__init__(nome,eta)
        
    
    def fai_suono(self):
        print(f"{self.nome} emette un suono")

    def bruca(self):
        print(f"{self.nome} bruca le foglie.")
        
    
        
class Pinguino(Animale):
    def __init__(self,nome,eta):
        super().__init__(nome,eta)
        
    def fai_suono(self):
        print(f"{self.nome} emette un suono")

    def nuota(self):
        print(f"{self.nome} sta nuotando spensierato.")
        
leone=Leone("Aria",5)
leone.fai_suono()
leone.caccia()
leone.informazioni()


        


        

    