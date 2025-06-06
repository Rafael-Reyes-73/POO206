lista = []
C=10
for C in range(201):
    if C==0:
        continue
    elif C%5==0 or C==200:
        lista.append(C)   
print(lista)