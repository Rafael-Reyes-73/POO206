try:
 numero = int(input ("Ingresa un numero: "))

 if numero%2:
     print("EL NUMERO ES IMPAR")     
 else:
     print("El NUMERO ES PAR")
  
except ValueError:
 print ("Error: Se ingreso un caracter")
