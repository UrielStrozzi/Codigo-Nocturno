class FichaMedica:
    def __init__(self, nro: int, observaciones: str, fechaalta: str, tratamientos, consulta, estado: int = 0):
        self.nro = nro
        self.observaciones = observaciones
        self.fechaalta = fechaalta
        self.fechabaja = ""
        self.tratamientos: list[int] = []
        self.consulta: list[int] = []
        self.tratamientos.append(tratamientos)
        self.consulta.append(consulta)
        self.estado = estado

    def __str__(self):
        return f"{self.nro};{self.observaciones};{self.fecha};{self.tratamientos};{self.consulta};{self.estado}"

    def __repr__(self):
        return self.__str__()

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self, fechabaja):
        self.estado = 0
        self.fechabaja = fechabaja

    def is_estado(self):
        return self.estado

    def modificar_datos(self, posicion, dato):
        if posicion == 1:
            self.nro = dato
        elif posicion == 2:
            self.observaciones = dato
        elif posicion == 3:
            self.fecha = dato
        elif posicion == 4:
            self.tratamientos = dato
        elif posicion == 5:
            self.consulta = dato
    def agregar_datos(self, posicion, dato):
        if posicion == 1:
            self.tratamientos.append(dato)
        elif posicion == 3:
            self.consulta.append(dato)


    def remover_datos(self, posicion, dato):
        if posicion == 1:
            self.tratamientos.remove(dato)
        elif posicion == 3:
            self.consulta.remove(dato)
