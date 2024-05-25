#HAZ UNA SUMA PARA APREDNER EN POCO TIEMPO

import time
import random

aciertos=0
tiempoinicio=time.time()

for i in range(5):
    numero1= random.randint(1, 20)
    numero2= random.randint(1, 20)
    correcto=numero1+numero2
    
    respuesta=int(input(f"Cuanto es {numero1} + {numero2} es?: "))
    
    if respuesta == correcto:
        print("CORRECTO")
    else:
        print(f"INCORRECTO ..... EL NUMERO CORRECTO ES: {correcto}")

tiempototal=time.time()-tiempoinicio
print(f"Haz tardado {tiempototal: .2f} segundos")
    


    
    