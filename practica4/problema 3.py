"""3. Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase."""

frase = input("Escribe una frase: ")

while True:
    letra = input("Escribe una letra: ")
    if len(letra) != 1:
        print("Error: Debes ingresar exactamente una letra.")
    else:
        break

C = 0
for i in frase:
    if i == letra:
        C += 1

print("La letra", letra, "aparece", C, "veces en la frase.")