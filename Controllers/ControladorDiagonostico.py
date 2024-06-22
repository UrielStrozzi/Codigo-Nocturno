from View.VistaDiagnostico import VistaDiagnostico
from Models.Diagnostico import Diagnostico


class ControladorDiagnostico:
    def __init__(self):
        self.vista = VistaDiagnostico()
        self.listadiagnostico: list[Diagnostico] = []

    def cargardiagnostico(self):
        try:
            file = open("Txt/diagnostico.txt",encoding='utf-8')
            for line in file:
                var1 = line.strip().split(",")
                self.listadiagnostico.append(Diagnostico(int(var1[0]), var1[1], var1[2]))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def agregardiagnostico(self):
        self.listadiagnostico.append(Diagnostico(self.vista.solicitarcodigo(), self.vista.solicitartipo(), self.vista.solicitardescripcion()))
        self.listadiagnostico[-1].dar_alta()
        self.vista.mostrarmensaje(1)

    def ver_lista_diagnosticos(self):
        self.vista.mostrardiagnostico(self.listadiagnostico)

    def modificardiagnostico(self):
        self.vista.mostrardiagnostico(self.listadiagnostico)
        self.vista.mostrarmensaje(2)
        codigo = self.vista.solicitarcodigo()
        for diagnostico in self.listadiagnostico:
            if diagnostico.nro == codigo:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                diagnostico.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminardiagnostico(self):
        self.vista.mostrardiagnostico(self.listadiagnostico)
        self.vista.mostrarmensaje(5)
        codigodiagnostico = self.vista.solicitarcodigo()
        for diagnostico in self.listadiagnostico:
            if diagnostico.nro == codigodiagnostico:
                self.listadiagnostico[self.listadiagnostico.index(diagnostico)].dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def guardardiagnostico(self):
        guardado = ""
        for diagnostico in self.listadiagnostico:
            guardado += f"{diagnostico}\n"
        file = open("Txt/diagnostico.txt", "r+")
        file.write(guardado[0:-1])
        file.close()
