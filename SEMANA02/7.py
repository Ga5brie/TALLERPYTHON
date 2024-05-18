#esribir un program qie almacene el diccionario con los creditos de las
#asignaturas de un curso {"matematica": 6 , "fisica": 4 , "quimica" : 5}
#y despues muestre por pantalla los creditos de cada asignatura 

curso={"matematica": 6 , "fisica": 4 , "quimica" : 5}
total_creditos=0
for asignatura, credito in curso.items():
    print(asignatura, "tiene", credito, "creditos")
    total_creditos+= credito
print("NUmero total de creditos: ",total_creditos)