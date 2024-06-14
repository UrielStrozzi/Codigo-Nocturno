class Raza:
    def __init__(self, nombre:str, colores_tipicos:str, tamano:str, pelaje:str, estado = 0):
        self.nombre = nombre
        self.colores_tipicos = colores_tipicos
        self.tamano = tamano
        self.pelaje = pelaje
        self.estado = estado

    def __str__(self):
        return f"{self.nombre},{self.colores_tipicos},{self.tamano},{self.pelaje},{self.estado}"

    def __repr__(self):
        return f"{self.nombre},{self.colores_tipicos},{self.tamano},{self.pelaje},{self.estado}"

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
            self.tamano = dato
        elif posicion == "3":
            self.pelaje = dato
