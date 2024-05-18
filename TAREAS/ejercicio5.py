#Ejercicio6
#Solicita aun usuraio 3 numero de los cuales debe de indicar cual es el mayor
print("Hola Usuario")
num1=int(input("Ingrese el 1 numero:"))
num2=int(input("Ingrese el 2 numero:"))
num3=int(input("Ingrese el 3 numero:"))
if num1>num2 and num1>num3:
    print(f"El numero {num1} es el mayor de todos")
elif num2>num1 and num2> num3:
    print(f"El numero {num2} es el mayor de todos")
else:
    print(f"El numero {num3} es el mayor de todos")