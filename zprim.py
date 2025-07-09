while True:
    numero = input("Escribe un número: ").strip()
    
    if numero == "":
        print("Campo vacío")
        continue

    try:
        numero = int(numero)
        
        if numero < 2:
            print("El número no es primo")
        else:
            es_primo = True
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            
            if es_primo:
                print("El número es primo")
            else:
                print("El número no es primo")
    
    except ValueError:
        print("El valor no es numérico")
