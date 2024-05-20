class Persona:
    def __init__(self, nombre, apellido, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.estado = 0
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.direccion}{self.estado}{self.telefono}"

    def __repr__(self):
        return f"{self.nombre}{self.apellido}{self.direccion}{self.estado}{self.telefono}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def is_estado(self):
        return self.estado

    def modificar_datos(self, posicion, dato):
        if posicion == "0":
            self.nombre = dato
        elif posicion == "1":
            self.apellido = dato
        elif posicion == "2":
            self.direccion = dato
        elif posicion == "3":
            self.telefono = dato
    def ver_lista_diagnostico(self):
        pass
