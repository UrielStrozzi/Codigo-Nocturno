from Models.Persona import Persona


class Cliente(Persona):
    def __init__(self, nro: int, nombre: str, apellido: str, direccion: str, telefono: int, estado: int = 0):
        super().__init__(nombre, apellido, direccion, telefono, estado)
        self.nro = nro

    def __str__(self):
        return f"{self.nro},{super().__str__()}"

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
        super().modificar_datos(posicion, dato)
