#Crear un programa que pregunte al usuario la cantidad a invertir, en interes anual 
#y el numero de años, y muestre por la pantalla el capital obtenido en la inversion 
#cada año que dura la inversion

inversion=int(input("Ingrese el capital a invertir: "))
interes=int(input("Ingrese el interes anual: "))
tiempo=int(input("Ingrese los tiempo(años): "))
print("")

for i in range(0, tiempo):
    resultado=(inversion)*(1+interes)**tiempo

print("El capital final de tu inversion de: " ,inversion, " en ",tiempo, "año es: " ,resultado)
    
    
    
