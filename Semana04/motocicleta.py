from vehiculo import vehiculo

class motocicleta(vehiculo):
    def __init__(self, marca, modelo, año, tipo_modelo ):
        super().__init__(marca, modelo, año)
        self.tipo_modelo=tipo_modelo
    
    def mostar_info(self):
        super().mostar_info()
        print(f"Tipo de modelo: {self.tipo_modelo}")