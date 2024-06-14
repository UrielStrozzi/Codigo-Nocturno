class Diagnostico:
    def __init__(self, codigo:int, tipo:str,descripcion:list,estado:int=0):
        self.codigo = codigo
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"{self.codigo},{self.tipo},{self.descripcion}"

    def __repr__(self):
        return f"{self.codigo},{self.tipo},{self.descripcion}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def modificar_datos(self, posicion, dato):
        if posicion == "1":
            self.codigo = dato
        elif posicion == "2":
            self.tipo = dato
        elif posicion == "3":
            self.descripcion = dato


    def calcularRankingDiagnostico(self):
        pass
    def calcularCantRazaXdiagnos(self):
        pass
