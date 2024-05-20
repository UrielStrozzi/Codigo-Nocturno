class Consulta:
    def __init__(self, cliente, veterinario, tratamiento, diagnostico, vacuna):
        self.cliente = cliente
        self.veterinario = veterinario
        self.tratamiento = tratamiento
        self.diagnostico = diagnostico
        self.estado = 0
        self.vacuna = vacuna

    def __str__(self):
        return f"{self.cliente}{self.veterinario}{self.tratamiento}{self.diagnostico}{self.estado}{self.vacuna}"

    def __repr__(self):
        return f"{self.cliente}{self.veterinario}{self.tratamiento}{self.diagnostico}{self.estado}{self.vacuna}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def is_estado(self):
        return self.estado

    def modificar_datos(self, posicion, dato):
        if posicion == "0":
            self.cliente = dato
        elif posicion == "1":
            self.veterinario = dato
        elif posicion == "2":
            self.tratamiento = dato
        elif posicion == "3":
            self.diagnostico = dato
        elif posicion == "4":
            self.vacuna = dato

    def calcular_cant_mascotas_por_cliente(self):
        pass

    def calcular_cant_consulta_por_cliente(self):
        pass
