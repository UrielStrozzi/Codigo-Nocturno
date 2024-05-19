class Tratamiento:
    def __init__(self, tipo="", detalleTratamiento=[],estado=0):
        self.tipo = tipo
        self.detalleTratamiento = detalleTratamiento
        self.esado = estado

    def __str__(self):
        return f"{self.tipo} {self.estado}"
    def __repr__(self):
        return f"{self.tipo} {self.estado}"

    def dar_baja(self, estado):
        pass

    def modificar(self):
        pass

    def dar_alta(self):
        pass

    def verListaTraramiento(self):
        pass

    def calcularTratamientoAplicados(self):
        pass