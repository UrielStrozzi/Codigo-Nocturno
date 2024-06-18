from View.VistaFichaMedica import VistaFichaMedica
from Models.FichaMedica import FichaMedica
from Models.Cliente import Cliente
from Models.Consulta import Consulta
from Models.Tratamiento import Tratamiento


class ControladorFichaMedica:
    def __init__(self):
        self.vista = VistaFichaMedica()
        self.listafichamedica: list[FichaMedica] = []
        self.cargarfichamedica()

    def agregarfichamedica(self,listafichamedica,listatratamientos: list[Tratamiento], listaconsulta: list[Consulta]):
        nrofichamedica = self.vista.solicitarnro()
        nrotratamiento = self.vista.solicitartratamiento()
        nroconsulta = self.vista.solicitarconsulta()
        opcion = -1
        for fichamedica in listafichamedica:
            if fichamedica.nro == nrofichamedica:
                for tratamiento in listatratamientos:
                    if tratamiento.nro == nrotratamiento:
                        for consulta in listaconsulta:
                            if consulta.nro == nroconsulta:
                                self.listafichamedica.append(FichaMedica(self.vista.solicitarnro(),
                                                                   self.vista.solicitarobservacion(),
                                                                   self.vista.solicitartratamiento(),
                                                                   self.vista.solicitarconsulta()))
        while opcion != 0:
            self.vista.mostrarmensaje(9)
            opcion = self.vista.solicitaropcion()
            if opcion == 1:
                nrotratamiento = self.vista.solicitartratamiento()
                for tratamiento in listatratamientos:
                    if tratamiento.nro == nrotratamiento:
                        self.listafichamedica[-1].agregar_datos(opcion, nrotratamiento)
            elif opcion == 2:
                nroconsulta = self.vista.solicitarconsulta()
                for consulta in listaconsulta:
                    if consulta.nro == nroconsulta:
                        self.listafichamedica[-1].agregar_datos(opcion, nroconsulta)
            elif opcion == 0:
                self.listaconsulta[-1].dar_alta()
                self.vista.mostrarmensaje(1)
            else:
                self.vista.mostrarmensaje(10)

    def modificarfichamedica(self,
                          listatratamientos: list[Tratamiento],listaconsulta: list[Consulta]):
        self.vista.mostrarfichamedica(self.listafichamedica)
        self.vista.mostrarmensaje(2)
        nrofichamedica = self.vista.solicitarnro()
        for ficha in self.listafichamedica:
            if ficha.nro == nrofichamedica:
                self.vista.mostrarmensaje(11)
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                if cambio in (1, 2, 3):
                    ficha.modificar_datos(cambio, nuevo_valor)
                elif cambio == 4:
                    for tratamiento in listatratamientos:
                        if tratamiento.nro == nuevo_valor:
                            self.listafichamedica[self.listafichamedica.index(tratamiento)].modificar_datos(cambio, nuevo_valor)

                elif cambio == 5:
                    for consulta in listaconsulta:
                        if consulta.nro == nuevo_valor:
                            self.listafichamedica[self.listafichamedica.index(consulta)].modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminarfichamedica(self):
        self.vista.mostrarfichamedica(self.listafichamedica)
        self.vista.mostrarmensaje(5)
        nrofichamedica = self.vista.solicitarnro()
        for ficha in self.listafichamedica:
            if ficha.nro == nrofichamedica:
                self.listafichamedica[self.listafichamedica.index(ficha)].dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def cargarfichamedica(self):
        try:
            file = open("Txt/fichamedica.txt")
            for line in file:
                var1 = line.strip().split(";")
                var1[3] = var1[3][1:-1].split(",")
                var1[4] = var1[4][1:-1].split(",")
                self.listafichamedica.append(
                    FichaMedica(int(var1[0]), var1[1], var1[2], int(var1[3][0]), int(var1[4][0]), int(var1[5])))
                for i in var1[3][1:]:
                    self.listafichamedica[-1].agregar_datos(1, int(i))
                for i in var1[4][1:]:
                    self.listafichamedica[-1].agregar_datos(2, int(i))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarconsulta(self):
        guardado = ""
        for ficha in self.listafichamedica:
            guardado += f"{ficha}\n"
        file = open("Txt/fichamedica.txt", "r+")
        file.write(guardado[0:-1])
        file.close()

    def ver_lista_fichamedica(self):
        self.vista.mostrarfichamedica(self.listafichamedica)
