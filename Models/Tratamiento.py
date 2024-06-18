class Tratamiento:
    def __init__(self, nro: int, tipo: str, detalletratamiento: str, estado: int = 0):
        self.nro = nro
        self.tipo = tipo
        self.detalletratamiento = detalletratamiento
        self.estado = estado

    def __str__(self):
        return f"{self.nro},{self.tipo},{self.detalletratamiento},{self.estado}"

    def __repr__(self):
        return f"{self.__str__()}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def modificar_datos(self, posicion, dato):
        if posicion == "1":
            self.nro = dato
        elif posicion == "2":
            self.tipo = dato
        elif posicion == "3":
            self.detalletratamiento = dato
