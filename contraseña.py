try:
    contraseña = input("Ingresa una contraseña: ").strip()

    if not contraseña:
        raise ValueError("No ingresaste ninguna contraseña")

    if len(contraseña) < 10:
        print("Contraseña demasiado corta")
    else:
        hay_numero = False
        hay_especial = False

        for letra in contraseña:
            if letra >= '0' and letra <= '9':
                hay_numero = True
            if not (letra.isalpha() or letra.isdigit()):
                hay_especial = True

        if not hay_numero:
            print("Debe contener al menos un número")
        elif not hay_especial:
            print("Debe contener al menos un carácter especial")
        else:
            print("Contraseña válida")

except ValueError as ma:
    print("Error:", ma)
