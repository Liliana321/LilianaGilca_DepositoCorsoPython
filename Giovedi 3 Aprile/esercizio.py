
# Esercizio 1
""" Crea una classe chiamata Punto. Questa classe dovrebbe avere:

Due attributi: x e y, per rappresentare le coordinate del punto nel piano.

Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.

Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano


 """
import math

class Punto:  # Dichiaro la classe
    
    def __init__(self, x, y):  # Metodo costruttore per inizializzare l'oggetto
        self.x = x  # Attributo di istanza 
        self.y = y  # Attributo di istanza 

    def muovi(self,dx,dy):  # Metodo 'muovi' per modificare le coordinate del punt
        self.x+=dx # la coordinata x del punto viene aumentata del valore dx
        self.y+=dy # la coordinata y del punto viene aumentata
    def distanza_da_origine(self):
        distanza=math.sqrt(self.x**2+self.y**2)
        return distanza

punto = Punto(0, 0)
print(f"Coordinate iniziali: ({punto.x}, {punto.y})")
punto.muovi(1, -2)
print(f"Coordinate dopo il movimento: ({punto.x}, {punto.y})")
print(f"Distanza dall'origine: {punto.distanza_da_origine()}")
        
