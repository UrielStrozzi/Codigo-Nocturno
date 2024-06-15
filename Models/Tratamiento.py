class Tratamiento:
    def __init__(self, codigo: int, tipo: str, detalleTratamiento: str, estado: int = 0):
        self.codigo = codigo
        self.tipo = tipo
        self.detalleTratamiento = detalleTratamiento
        self.estado = estado

    def __str__(self):
        return f"{self.codigo},{self.tipo},{self.detalleTratamiento},{self.estado}"

    def __repr__(self):
        return self.__str__()

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def modificar_datos(self, posicion, dato):
        if posicion == "1":
            self.codigo = dato
        elif posicion == "2":
            self.tipo = dato
        elif posicion == "3":
            self.detalleTratamiento = dato
