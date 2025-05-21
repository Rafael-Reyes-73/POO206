def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print(f"Tienes {edad} años.")

try:
    edad_usuario = int(input("Introduce tu edad: "))
    validar_edad(edad_usuario)
except ValueError as e:
    print(f"Error: {e}")
