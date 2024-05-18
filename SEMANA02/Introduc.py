#Bucles
#for, while, do-while

#condicionales
#if, switch

#Escribir un numero que pida al usuario un numero entero positivo
# y que muestres por pantalla todos los numeros impares desde 1
#hasta ese numero separados por comas
n = int(input("INTRODUCE UN NUMERO ENTERO POSITIVIO:"))
for i in range (1, n+1, 2):
    print(i, end=",")