while True:
    try:
        pala = input("Ingresa una palabra: ").strip()
        if not pala:
            raise ValueError("No se ingresó ningún texto.")
        
        pala = pala.replace(" ", "").lower()

        if pala == pala[::-1]:
            print("Es un palíndromo")
        else:
            print("No es un palíndromo")
        
        while True:
            opcion = input("¿Quieres probar con otra palabra? (s/n): ").lower()
            if opcion == 's':
                break 
            elif opcion == 'n':
                exit()
            else:
                print("Ingresa 's' para sí o 'n' para no.")
    except ValueError as ma:
        print("Error:", ma)
    except Exception as ru:
        print("Ocurrió un error inesperado:", ru)
