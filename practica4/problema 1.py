"""1. Escribir un programa que pida al usuario un número entero positivo mayor de 10 y
que muestre como resultado todos los números impares desde 2 hasta ese número
separados por comas. """

while True:
    try:
        numero = int(input("Escribe un número > 10: "))
        if numero <= 10:
            print("Error: El número debe ser mayor que 10.")
        else:
            break
    except ValueError:
        print("Error: Ingresa un número entero válido.")

vec = []
C = 1

for i in range(numero):
    C += 1
    if C % 2 == 0:
        vec.append(C)

print("Lista de números pares:", vec)