
import numpy as np

# Creazione di un array
array = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indici = np.array([1, 3])
print(array[indici])  # Output: [20 40]

# Utilizzo di una lista di indici
indici = [0, 2, 4]
print(array[indici])  # Output: [10 30 50]
