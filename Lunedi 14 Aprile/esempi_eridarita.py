# Classe base
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print(f"{self.nome} fa suono generico.")

# Classe derivata (eredita da Animale) 
class Cane(Animale): # la classe che prende riferimento dall'Animale
    def parla(self):
        print(f"{self.nome} abbaia!")

# Creazione degli oggetti
animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

# Chiamata ai metodi
animale_generico.parla()  # Output: AnimaleGenerico fa suono generico.
cane.parla()              # Output: Fido abbaia!


