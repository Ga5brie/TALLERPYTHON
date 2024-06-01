from vehiculo import vehiculo

class camion(vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga=capacidad_carga
    
    def mostar_info(self):
        super().mostar_info()
        print(f"Capacidad de carga: {self.capacidad_carga}")