#Escribir un programa en el que se le pregunte al usuario por una frase
#y una letra y muestre en por la pantalla el numero de veces que
#aparece la letra en la frase

frase=input("Introduce la frase: ")
letra=input("Introduce la letra: ")
contador=0

for i in frase:
    if i==letra:
        contador+=1
print(f"La letra {letra} aparece {contador} en la frase -> {frase}")
print("La letra ´%s´ aparece %2i veces en la frase ´%s´." % (letra, contador,frase))

print(contador)