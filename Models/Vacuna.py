class Vacuna:
    def __init__(self,nombre:str,tipo:str,precio:float, estado:int = 0):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.estado = estado


    def __str__(self):
        return f"{self.nombre},{self.tipo}, {self.precio}, {self.estado}"
    def __repr__(self):
        return f"{self.nombre},{self.tipo}, {self.precio}, {self.estado}"

    def dar_baja(self):
        self.estado = 0

    def modificar(self):
        pass

    def dar_alta(self):
        self.estado = 1

    def lista_vacunas(self):
        pass

    def modificar_datos(self, posicion, dato):
        if posicion == "0":
            self.nombre = dato
        elif posicion == "1":
            self.tipo = dato
        elif posicion == "2":
            self.precio = dato
