class Raza:
    def __init__(self, nombre, colores_tipicos, tamaño, pelaje):
        self.nombre = nombre
        self.colores_tipicos = colores_tipicos
        self.tamaño = tamaño
        self.pelaje = pelaje
        self.estado = 0

    def __str__(self):
        return f"{self.nombre}{self.colores_tipicos}{self.tamaño}{self.pelaje}{self.estado}"

    def __repr__(self):
        return f"{self.nombre}{self.colores_tipicos}{self.tamaño}{self.pelaje}{self.estado}"

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
            self.colores_tipicos = dato
        elif posicion == "2":
            self.tamaño = dato
        elif posicion == "3":
            self.pelaje = dato

    def ver_razas(self):
        pass
