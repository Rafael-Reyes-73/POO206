while True:
    año = input("Introduce un año: ").strip()

    if año == "":
        print("Error: No ingresaste ningún valor.")
        continue

    try:
        año = int(año)
        if año == 0:
            print("programa terminado.")
            break
        elif (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print("El año:", año, "Es bisiesto")
        else:
            print("El año:", año, "No bisiesto")
    except ValueError:
        print("Error: Se ingresó algo que no es un año.")

