
'''
classe per le statistiche 
'''
import numpy as np


class analisi_st:
    def __init__(self, data):
        """
        Inizializza l'oggetto con un array di dati numerici.
        Converte i dati in un array NumPy di tipo float.
        """
        self.data = np.array(data, dtype=float)

    def mean(self):
        """Restituisce la media aritmetica dei dati."""
        return np.mean(self.data)

    def median(self):
        """Restituisce la mediana dei dati."""
        return np.median(self.data)


    def variance(self):
        """Restituisce la varianza (dispersione dei dati)."""
        return np.var(self.data)

    def standard_deviation(self):
        """Restituisce la deviazione standard."""
        return np.std(self.data)



