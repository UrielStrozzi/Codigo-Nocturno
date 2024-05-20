import Persona


class Veterinario(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, especializacion, nro_matricula):
        super().__init__(nombre, apellido, direccion, telefono)
        self.especializacion = especializacion
        self.nro_matricula = nro_matricula

    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.direccion}{self.estado}{self.telefono}{self.especializacion}{self.nro_matricula}"

    def __repr__(self):
        return f"{self.nombre}{self.apellido}{self.direccion}{self.estado}{self.telefono}{self.especializacion}{self.nro_matricula}"

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
        elif posicion == "4":
            self.especializacion = dato
        elif posicion == "5":
            self.nro_matricula = dato

    def mostrar_veterinario(self):
        pass

    def ver_lista_veterinario(self):
        pass