def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operación finalizada.")

dividir(8, 0)
