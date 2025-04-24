import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

# Imposta la dimensione predefinita delle figure (larghezza, altezza in pollici)
plt.rcParams['figure.figsize'] = [10, 6]

# Imposta la risoluzione delle figure in DPI (dots per inch)
plt.rcParams['figure.dpi'] = 100

# Imposta il colore di sfondo della figura
plt.rcParams['figure.facecolor'] = 'white'


# Configura Seaborn
sns.set_theme(style="darkgrid")

# Crea alcuni dati
data = np.random.normal(size=100)

# Crea un grafico
""" sns.histplot(data, kde=True)
plt.title('Distribuzione dei dati')
plt.show() """


""" fig=plt.figure()
ax=fig.add_subplot(111) """



# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.figure()
# plt.plot(x, y)
# plt.title('Grafico a Linee')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.show()

# categories = ['A', 'B', 'C', 'D', 'E']
# values = [3, 7, 2, 5, 8]

# plt.figure()
# plt.bar(categories, values)
# plt.title('Grafico a Barre')
# plt.xlabel('Categorie')
# plt.ylabel('Valori')
# plt.show()


data = np.random.randn(1000) 
# genera un array di 1000 numeri casuali estratti da una distribuzione
# normale standard (

# plt.figure()
# plt.hist(data, bins=30)
# plt.title('Istogramma')
# plt.xlabel('Valori')
# plt.ylabel('Frequenza')
# plt.show()

# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.figure()
# plt.scatter(x, y)
# plt.title('Scatter Plot')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.show()


# # Dati di esempio
# tips = sns.load_dataset("tips")

# # Creare un grafico a barre con media dei conti totali per giorno
# sns.barplot(x="day", y="total_bill", data=tips, estimator=sum)

# # Titolo del grafico
# plt.title('Conto Totale per Giorno')

# # Mostrare il grafico
# plt.show()

# Dati di esempio
fmri = sns.load_dataset("fmri")
# Creare un grafico a linee
sns.lineplot(x="timepoint", y="signal", data=fmri, hue="region", style="event")


plt.title('Segnale FMRI nel Tempo')
plt.show()



