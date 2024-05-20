import Persona


class Cliente(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, nro_mascota):
        super().__init__(nombre, apellido, direccion, telefono)
        self.nro_mascota = nro_mascota

    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.direccion}{self.estado}{self.telefono}{self.nro_mascota}"

    def __repr__(self):
        return f"{self.nombre}{self.apellido}{self.direccion}{self.estado}{self.telefono}{self.nro_mascota}"

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
            self.nro_mascota = dato

    def mostrar_cliente(self):
        pass

    def ver_lista_clientes(self):
        pass

    def consultar_cant_mascotas(self):
        pass

