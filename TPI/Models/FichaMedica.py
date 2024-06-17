from datetime import datetime

class FichaMedica:
    def __init__(self, nro: int, observacion: str, mascota, tratamiento, consulta, estado: int = 0):
        self.nro = nro
        self.obsevarcion = observacion
        self.mascota = mascota
        self.fecha = datetime.now().date()
        self.tratamiento = tratamiento
        self.consulta = consulta
        self.fecha_alta = ""
        self.estado = estado

    def __str__(self):
        return f"{self.nro},{self.obsevarcion},{self.fecha},{self.mascota},{self.tratamiento},{self.consulta},{self.fecha_alta},{self.estado}"

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
        elif posicion == "2":
            self.obsevarcion = dato
        elif posicion == "3":
            self.mascota = dato
        elif posicion == "4":
            self.tratamiento = dato
        elif posicion == "5":
            self.consulta = dato
