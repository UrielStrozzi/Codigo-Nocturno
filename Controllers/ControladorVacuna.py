from View.VistaVacuna import VistaVacuna
from Models.Vacuna import Vacuna


class ControladorVacuna:
    def __init__(self):
        self.vista = VistaVacuna()
        self.listavacunas: list[Vacuna] = []
        self.cargarvacunas()

    def agregarvacuna(self):
        self.listavacunas.append(Vacuna(self.vista.solicitarnombre(), self.vista.solicitartipo(), self.vista.solicitarprecio()))
        self.listavacunas[-1].dar_alta()
        self.vista.mostrarmensaje(1)

    def modificarvacuna(self):
        self.vista.mostrarvacunas(self.listavacunas)
        self.vista.mostrarmensaje(2)
        nombrevacuna = self.vista.solicitarnombre()
        for vacuna in self.listavacunas:
            if vacuna.nombre == nombrevacuna:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                vacuna.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
                return
        self.vista.mostrarmensaje(4)

    def eliminarvacuna(self):
        self.vista.mostrarvacunas(self.listavacunas)
        self.vista.mostrarmensaje(5)
        nombrevacuna = self.vista.solicitarnombre()
        for vacuna in self.listavacunas:
            if vacuna.nombre == nombrevacuna:
                self.listavacunas[self.listavacunas.index(vacuna)].dar_baja()
                self.vista.mostrarmensaje(6)
                return
        self.vista.mostrarmensaje(7)

    def cargarvacunas(self):
        try:
            file = open("Txt/vacuna.txt")
            for line in file:
                var1 = line.strip().split(",")
                self.listavacunas.append(Vacuna(var1[0], var1[1], var1[2]))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarvacunas(self):
        file = open("vacuna.txt", "w")
        guardado = ""
        for vacuna in self.listavacunas:
            guardado += f"{vacuna}\n"
        file.write(guardado[0:-2])
        file.close()

    def ver_lista_vacuna(self):
        self.vista.mostrarvacunas(self.listavacunas)
