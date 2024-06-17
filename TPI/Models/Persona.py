class Persona:
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: int, estado: int = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.estado = estado

    def __str__(self):
        return f"{self.nombre},{self.apellido},{self.direccion},{self.telefono},{self.estado}"

    def __repr__(self):
        return f"{self.__str__()}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def is_estado(self):
        return self.estado

    def modificar_datos(self, posicion, dato):
        if posicion == "2":
            self.nombre = dato
        elif posicion == "3":
            self.apellido = dato
        elif posicion == "4":
            self.direccion = dato
        elif posicion == "5":
            self.telefono = dato
