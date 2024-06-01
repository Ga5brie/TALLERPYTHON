from vehiculo import vehiculo

class coche(vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas=puertas
    
    def mostar_info(self):
        super().mostar_info()
        print(f"Puertas: {self.puertas}")