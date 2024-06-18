from Models.Persona import Persona


class Veterinario(Persona):
    def __init__(self, nro_matricula: int, nombre: str, apellido: str, direccion: str, telefono: int, especializacion: str, estado: int = 0):
        super().__init__(nombre, apellido, direccion, telefono, estado)
        self.especializacion = especializacion
        self.nro_matricula = nro_matricula

    def __str__(self):
        return f"{self.nro_matricula},{super().__str__()},{self.especializacion}"

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
            self.nro_matricula = dato
        super().modificar_datos(posicion, dato)
        if posicion == "6":
            self.especializacion = dato
