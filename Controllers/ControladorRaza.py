from View.VistaRaza import VistaRaza
from Models.Raza import Raza


class ControladorRaza:
    def __init__(self):
        self.vista = VistaRaza()
        self.listarazas: list[Raza] = []
        self.cargarrazas()

    def agregarraza(self):
        self.listarazas.append(Raza(self.vista.solicitarnombre(), self.vista.solicitarcolor(), self.vista.solicitartamano(), self.vista.solicitarpelaje()))
        self.listarazas[-1].dar_alta()
        self.vista.mostrarmensaje(1)

    def modificarraza(self):
        self.vista.mostrarraza(self.listarazas)
        self.vista.mostrarmensaje(2)
        nombreraza = self.vista.solicitarnombre()
        for raza in self.listarazas:
            if raza.nombre == nombreraza:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                raza.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
                return
        self.vista.mostrarmensaje(4)

    def eliminarraza(self):
        self.vista.mostrarraza(self.listarazas)
        self.vista.mostrarmensaje(5)
        nombreraza = self.vista.solicitarnombre()
        for raza in self.listarazas:
            if raza.nombre == nombreraza:
                self.listarazas[self.listarazas.index(raza)].dar_baja()
                self.vista.mostrarmensaje(6)
                return
        self.vista.mostrarmensaje(7)

    def cargarrazas(self):
        try:
            file = open("Txt/raza.txt")
            for line in file:
                var1 = line.strip().split(",")
                self.listarazas.append(Raza(var1[0], var1[1], var1[2], var1[3], var1[4]))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarrazas(self):
        guardado = ""
        for raza in self.listarazas:
            guardado += f"{raza}\n"
        file = open("Txt/raza.txt", "r+")
        file.write(guardado[0:-1])
        file.close()

    def ver_lista_razas(self):
        self.vista.mostrarraza(self.listarazas)
