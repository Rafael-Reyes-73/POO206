while True:
    numero = input("Ingresa un número: ").strip()

    if numero == "":
        print("Error: No ingresaste nada.")
        continue

    if numero == "0":
        break

    try:
        numero = int(numero)
        if numero % 2:
            print("El número es impar")
        else:
            print("El número es par")
    except ValueError:
        print("Error: Se ingresó un carácter no numérico.")
