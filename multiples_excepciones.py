try:
    lista = [1, 2, 3]
    indice = int(input("Introduce el índice que quieres ver: "))
    print(lista[indice])
except (ValueError, IndexError) as error:
    print(f"Erro ya sea por indice o por ingresar una letra o caracter: {error}")
#