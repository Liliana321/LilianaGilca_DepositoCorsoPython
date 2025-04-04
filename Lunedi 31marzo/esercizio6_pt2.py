a = int(input("Inserisci un primo numero: "))
b = int(input(f"Inserisci un secondo numero : "))

fattori_a=[]
fattori_b=[10]
fattori_comuni=[]

# troviamo i fattori di a
for i in range(1, a + 1):
    if a % i == 0:
        fattori_a.append(i)
    
# troviamo i fattori di b
for j in range(1, b + 1):
    if b % j == 0:
        fattori_b.append(j)
for i in fattori_a and j in fattori_b:
    if i==j:
        fattori_comuni.append(i)
    else:
        break
    