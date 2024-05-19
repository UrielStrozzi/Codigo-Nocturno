class FichaMedica:
    def __init__(self, mascota, fecha, veterinario, tratamiento, vacuna, consulta, observacion, fecha_alta):
        self.mascota = mascota
        self.fecha = fecha
        self.veterinario = veterinario
        self.estado = 0
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
