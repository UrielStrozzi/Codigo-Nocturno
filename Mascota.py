class Mascota:
    def __init__(self, nombre, fecha_nac, cliente, raza, ficha_medica):
        self.nombre = nombre
        self.estado = 0
        self.fecha_nac = fecha_nac
        self.cliente = cliente
        self.raza = raza
        self.ficha_medica = ficha_medica

    def __str__(self):
        return f"{self.nombre}{self.fecha_nac}{self.cliente}{self.raza}{self.ficha_medica}"

    def __repr__(self):
        return f"{self.nombre}{self.fecha_nac}{self.cliente}{self.raza}{self.ficha_medica}"

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
            self.fecha_nac = dato
        elif posicion == "2":
            self.raza = dato
        elif posicion == "3":
            self.cliente = dato
        elif posicion == "4":
            self.ficha_medica = dato

    def conocer_raza(self):
        pass

    def calcular_edad(self):
        pass

    def registrar(self):
        pass
