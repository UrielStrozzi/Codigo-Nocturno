class Consulta:
    def __init__(self, nro: int, observaciones: str, fecha: str, cliente: int, veterinario: int, diagnostico: int, estado: int = 0):
        self.nro = nro
        self.observaciones = observaciones
        self.fecha = fecha
        self.cliente = cliente
        self.veterinarios: list[int] = []
        self.diagnosticos: list[int] = []
        self.tratamientos: list[int] = []
        self.vacunas: list[int] = []
        self.veterinarios.append(veterinario)
        self.diagnosticos.append(diagnostico)
        self.estado = estado

    def __str__(self):
        return f"{self.nro};{self.observaciones};{self.fecha};{self.cliente};{self.veterinarios};{self.tratamientos};{self.diagnosticos};{self.vacunas};{self.estado}"

    def __repr__(self):
        return self.__str__()

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

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
            self.cliente = dato

    def agregar_datos(self, posicion, dato):
        if posicion == 1:
            self.veterinarios.append(dato)
        elif posicion == 3:
            self.tratamientos.append(dato)
        elif posicion == 2:
            self.diagnosticos.append(dato)
        elif posicion == 4:
            self.vacunas.append(dato)

    def remover_datos(self, posicion, dato):
        if posicion == 1:
            self.veterinarios.remove(dato)
        elif posicion == 3:
            self.tratamientos.remove(dato)
        elif posicion == 2:
            self.diagnosticos.remove(dato)
        elif posicion == 4:
            self.vacunas.remove(dato)
