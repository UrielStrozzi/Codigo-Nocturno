class Vacuna:
    def __init__(self, nro: int, nombre: str, tipo: str, precio: float, estado: int = 0):
        self.nro = nro
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.estado = estado

    def __str__(self):
        return f"{self.nro},{self.nombre},{self.tipo},{self.precio},{self.estado}"

    def __repr__(self):
        return f"{self.__str__()}"

    def dar_baja(self):
        self.estado = 0

    def dar_alta(self):
        self.estado = 1

    def modificar_datos(self, posicion, dato):
        if posicion == "1":
            self.nro = dato
        elif posicion == "2":
            self.nombre = dato
        elif posicion == "3":
            self.tipo = dato
        elif posicion == "4":
            self.precio = dato
