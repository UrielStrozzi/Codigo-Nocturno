class Mascota:
    def __init__(self, nro: int, nombre: str, fecha_nac: str, cliente: int, raza: int, estado: int = 0):
        self.nro = nro
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.nrocliente = cliente
        self.nroraza = raza
        self.estado = estado

    def __str__(self):
        return f"{self.nro},{self.nombre},{self.fecha_nac},{self.nrocliente},{self.raza},{self.estado}"

    def __repr__(self):
        return f"{self.__str__()}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def is_estado(self):
        return self.estado

    def modificar_datos(self, posicion, dato):
        if posicion == "1":
            self.nro = dato
        elif posicion == "2":
            self.nombre = dato
        elif posicion == "3":
            self.fecha_nac = dato
        elif posicion == "4":
            self.raza = dato
        elif posicion == "5":
            self.cliente = dato
