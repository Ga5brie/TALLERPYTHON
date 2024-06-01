from coche import coche
from motocicleta import motocicleta
from camion import camion

def main():
    
    coche= coche("AUDI", "R8", "COUPE", "2022")
    motocicleta= motocicleta("YAMAHA", "YAMAHA" "2019", "DEPORTIVO")
    camion= camion("VOLVO", "VOLVO", "2022", "4000")
    
    print("INFORMACION DEL COCHE: ")
    coche.mostrar_info()
    
    print("\nINFORMACION DE LA MOTOCICLETA: ")
    motocicleta.mostar_info()
    
    print("\nMOSTRAR DATOS DEL CAMINION: ")
    camion.mostrar_info()   
    
    
    
    
main()
