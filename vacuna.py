class Vacuna:
    def __init__(self,nombre="",tipo="",estado=0,precio=0.0):
        self.nombre = nombre
        self.tipo = tipo
        self. estado = estado
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} {self.estado}"
    def __repr__(self):
        return f"{self.nombre} {self.estado}"

    def dar_baja(self,estado):
        pass

    def modificar(self):
        pass
    def dar_alta(self):
        pass

    def lista_vacunas(self):
        pass