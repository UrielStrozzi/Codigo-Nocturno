class FichaMedica:
    def __init__(self, mascota, fecha, veterinario, tratamiento, vacuna, consulta, observacion, fecha_alta):
        self.mascota = mascota
        self.fecha = fecha
        self.veterinario = veterinario
        self.estado = 0
        self.tratamiento = tratamiento
        self.vacuna = vacuna
        self.consulta = consulta
        self.obsevarcion = observacion
        self.fecha_alta = fecha_alta

    def __str__(self):
        return f"{self.mascota}{self.fecha}{self.veterinario}{self.estado}{self.tratamiento}{self.vacuna}{self.consulta}{self.obsevarcion}{self.fecha_alta}"

    def __repr__(self):
        return f"{self.mascota}{self.fecha}{self.veterinario}{self.estado}{self.tratamiento}{self.vacuna}{self.consulta}{self.obsevarcion}{self.fecha_alta}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def is_estado(self):
        return self.estado

    def modificar_datos(self, posicion, dato):
        if posicion == "0":
            self.mascota = dato
        elif posicion == "1":
            self.fecha = dato
        elif posicion == "2":
            self.veterinario = dato
        elif posicion == "3":
            self.tratamiento = dato
        elif posicion == "4":
            self.vacuna = dato
        elif posicion == "5":
            self.consulta = dato
        elif posicion == "6":
            self.obsevarcion = dato
        elif posicion == "7":
            self.fecha_alta = dato

    def cargar_ficha(self):
        pass

    def buscar_mascota(self):
        pass

    def ver_consultas(self):
        pass
