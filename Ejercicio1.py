import math
#EJERCICIO N°1 
#SOLICITAR A UN USUSARIO DOS NUMERO Y REALIZAR LAS OPERACIONES BASICAS: 
print("Hola Usuario")
print("Se le solicitaria dos numeros")
num1=int(input("INGRESE EL 1 NUMERO: "))
num2=int(input("INGRESE EL 2 NUMERO: "))
suma= num1 + num2
resta= num1 - num2
multiplicacion= num1 * num2
division= num1 / num2
residuodivision= num1 % num2
divisionentero= math.floor(num1/num2)
print("La Suma es: ", suma)
print("La Resta es: ", resta)
print("La Multiplicacion es: ", multiplicacion)
print("La Division es: ", division)
print("La Residuo de la division es: ", residuodivision)
print("La Division entero es: ", divisionentero)
