#Ejercicio 4
#calcular si un numero es divisible por 3 o 5 
print("Hola Usuario")
print("Se le solicitara un numero")
num1=int(input("Ingrese un numero entero:"))
if num1 % 3 == 0 and num1 % 5 ==0:
    print(f"El Numero {num1} es Divisible por 3 y 5 ")
else :
    print(f"El Numero {num1} no es Divisible por 3 o 5 ")