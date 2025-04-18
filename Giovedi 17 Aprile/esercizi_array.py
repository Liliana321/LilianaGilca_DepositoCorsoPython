import numpy as np

# matrice 6x6

matrice=np.random.randint(0,101,size=(6,6)) 

print("La matrice iniziale ")
print (matrice)
print("-"*20)

sotto_matrice=matrice[:4,:4] # estrazione sutto matrice dall amatrice principale 
print("La sotto-matrice 4x4 ")
print (sotto_matrice)
print("-"*20)

#matrice_invertita=np.invert(sotto_matrice)

'''
invert--> x = -x - 1

'''

'''

Invertire righe	                np.flipud(matrice)
Invertire colonne	            np.fliplr(matrice)
Invertire righe + colonne	    np.flip(matrice)
Trasporre (righe ↔ colonne)	    np.transpose(matrice) o matrice.T
Ruotare di 90°	                np.rot90(matrice)

'''

matrice_invertita=np.flipud(sotto_matrice)
print("La sotto-matrice invertita 4x4 ")
print (matrice_invertita)
print("-"*20)


diag=np.diag(matrice_invertita)
print("La diagonale della sotto-matrice invertita 4x4 ")
print(diag)
print("-"*20)

matrice_invertita[matrice_invertita%3==0] =-1
print("La sotto-matrice invertita modificata [-1] 4x4 ")
print(matrice_invertita)
print("-"*20)