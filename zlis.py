lista = []

while True:   
    
    numero = input("Escribe un numero: ").strip()
    if numero == "":
        print("El campo esta vacion")
        continue
    try:
        numero = int(numero)
        lista.append(numero)
        print(numero)
    except ValueError:
        print("ingresaste un valor no numerico")
        
    if len(lista) == 5:
        break
print(lista)      
