class Diagnostico:
    def __init__(self, tipo="", estado=0,descripcion=[]):
        self.tipo = tipo
        self.estado = estado
        self.descripcion = descripcion

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

    def calcularRankingDiagnostico(self):
        pass
    def calcularCantRazaXdiagnos(self):
        pass