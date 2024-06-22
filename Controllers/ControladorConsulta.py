from View.VistaConsulta import VistaConsulta
from Models.Consulta import Consulta
from Models.Cliente import Cliente
from Models.Veterinario import Veterinario
from Models.Tratamiento import Tratamiento
from Models.Diagnostico import Diagnostico
from Models.Vacuna import Vacuna


class ControladorConsulta:
    def __init__(self):
        self.vista = VistaConsulta()
        self.listaconsulta: list[Consulta] = []

    def agregarconsulta(self, listaclientes: list[Cliente], listaveterinarios: list[Veterinario],
                        listatratamientos: list[Tratamiento], listadiagnosticos: list[Diagnostico],
                        listavacunas: list[Vacuna]):
        nrocliente = self.vista.solicitarcliente()
        nroveterinario = self.vista.solicitarveterinario()
        nrodiagnostico = self.vista.solicitardiagnostico()
        opcion = -1
        for cliente in listaclientes:
            if cliente.nro == nrocliente:
                for veterinario in listaveterinarios:
                    if veterinario.nro_matricula == nroveterinario:
                        for diagnostico in listadiagnosticos:
                            if diagnostico.nro == nrodiagnostico:
                                self.listaconsulta.append(Consulta(self.vista.solicitarnro(),
                                                                   self.vista.solicitarobservacion(),self.vista.solicitarfecha(),
                                                                   nrocliente, nroveterinario, nrodiagnostico))
                                self.listaconsulta[-1].dar_alta()
        while opcion != 0:
            self.vista.mostrarmensaje(9)
            opcion = self.vista.solicitaropcion()
            if opcion == 1:
                nro = self.vista.solicitarveterinario()
                for veterinario in listaveterinarios:
                    if veterinario.nro_matricula == nro:
                        self.listaconsulta[-1].agregar_datos(opcion, nro)
            elif opcion == 2:
                nro = self.vista.solicitardiagnostico()
                for diagnostico in listadiagnosticos:
                    if diagnostico.nro == nro:
                        self.listaconsulta[-1].agregar_datos(opcion, nro)
            elif opcion == 3:
                nro = self.vista.solicitartratamiento()
                for tratamientos in listatratamientos:
                    if tratamientos.nro == nro:
                        self.listaconsulta[-1].agregar_datos(opcion, nro)
            elif opcion == 4:
                nro = self.vista.solicitarvacuna()
                for vacuna in listavacunas:
                    if vacuna.nro == nro:
                        self.listaconsulta[-1].agregar_datos(opcion, nro)
            elif opcion == 0:
                self.listaconsulta[-1].dar_alta()
                self.vista.mostrarmensaje(1)
            else:
                self.vista.mostrarmensaje(10)

    def modificarconsulta(self, listaclientes: list[Cliente], listaveterinarios: list[Veterinario],
                          listatratamientos: list[Tratamiento], listadiagnosticos: list[Diagnostico],
                          listavacunas: list[Vacuna]):
        self.vista.mostrarconsulta(self.listaconsulta)
        self.vista.mostrarmensaje(2)
        nroconsulta = self.vista.solicitarnro()
        for consulta in self.listaconsulta:
            if consulta.nro == nroconsulta:
                self.vista.mostrarmensaje(11)
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                if cambio in (1, 2, 3):
                    consulta.modificar_datos(cambio, nuevo_valor)
                elif cambio == 4:
                    for cliente in listaclientes:
                        if cliente.nro == nuevo_valor:
                            self.listaconsulta[self.listaconsulta.index(consulta)].modificar_datos(cambio, nuevo_valor)
                elif cambio in (5, 6, 7, 8):
                    cambio -= 4
                    opcion = self.vista.solicitaranadiroquitar()
                    if opcion == 1:
                        if cambio == 1:
                            for veterinario in listaveterinarios:
                                if veterinario.nro_matricula == nuevo_valor:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].agregar_datos(cambio,
                                                                                                         nuevo_valor)
                        elif cambio == 2:
                            for diagnostico in listadiagnosticos:
                                if diagnostico.nro == nuevo_valor:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].agregar_datos(cambio,
                                                                                                         nuevo_valor)
                        elif cambio == 3:
                            for tratamientos in listatratamientos:
                                if tratamientos.nro == nuevo_valor:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].agregar_datos(cambio,
                                                                                                         nuevo_valor)
                        elif cambio == 4:
                            for vacuna in listavacunas:
                                if vacuna.nro == nuevo_valor:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].agregar_datos(cambio,
                                                                                                         nuevo_valor)
                    elif opcion == 0:
                        if cambio == 1:
                            for veterinario in listaveterinarios:
                                if veterinario.nro_matricula == nuevo_valor and len(listaveterinarios) > 1:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].remover_datos(cambio,
                                                                                                         nuevo_valor)
                        elif cambio == 2:
                            for diagnostico in listadiagnosticos:
                                if diagnostico.nro == nuevo_valor and len(listadiagnosticos) > 1:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].remover_datos(cambio,
                                                                                                         nuevo_valor)
                        elif cambio == 3:
                            for tratamientos in listatratamientos:
                                if tratamientos.nro == nuevo_valor:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].remover_datos(cambio,
                                                                                                         nuevo_valor)
                        elif cambio == 4:
                            for vacuna in listavacunas:
                                if vacuna.nro == nuevo_valor:
                                    self.listaconsulta[self.listaconsulta.index(consulta)].remover_datos(cambio,
                                                                                                         nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminarconsulta(self):
        self.vista.mostrarconsulta(self.listaconsulta)
        self.vista.mostrarmensaje(5)
        nroconsulta = self.vista.solicitarnro()
        for consulta in self.listaconsulta:
            if consulta.nro == nroconsulta:
                self.listaconsulta[self.listaconsulta.index(consulta)].dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def cargarconsultas(self):
        try:
            file = open("Txt/consulta.txt",encoding='utf-8')
            for line in file:
                var1 = line.strip().split(";")
                var1[4] = var1[4][1:-1].split(",")
                var1[5] = var1[5][1:-1].split(",")
                var1[6] = var1[6][1:-1].split(",")
                var1[7] = var1[7][1:-1].split(",")
                self.listaconsulta.append(
                    Consulta(int(var1[0]), var1[1], var1[2], int(var1[3]), int(var1[4][0]), int(var1[6][0]),
                             int(var1[8])))
                for i in var1[4][1:]:
                    if len(var1[4][1:]) != 0:
                        self.listaconsulta[-1].agregar_datos(1, int(i))
                for i in var1[5][1:]:
                    if len(var1[5][1:]) != 0:
                        self.listaconsulta[-1].agregar_datos(2, int(i))
                for i in var1[6]:
                    if len(var1[6]) != 0:
                        self.listaconsulta[-1].agregar_datos(3, int(i))
                for i in var1[7]:
                    if var1[7] == "":
                        self.listaconsulta[-1].agregar_datos(4, int(i))

            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarconsulta(self):
        guardado = ""
        for consulta in self.listaconsulta:
            guardado += f"{consulta}\n"
        file = open("Txt/consulta.txt", "r+")
        file.write(guardado[0:-1])
        file.close()

    def ver_lista_con(self):
        self.vista.mostrarconsulta(self.listaconsulta)
