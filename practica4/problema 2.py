"""2. Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla la cuenta atrás desde ese número hasta cero separados por comas """

while True:
    try:
        numero = int(input("Escribe un número entero positivo: "))
        if numero < 0:
            print("Error: Debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Error: Ingresa un número entero válido.")

for i in range(numero, -1, -1):
    if i != 0:
        print(i, end=", ")
    else:
        print(i)
