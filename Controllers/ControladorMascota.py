from View.VistaMascota import VistaMascota
from Models.Mascota import Mascota
from Models.Consulta import Consulta
from Models import Cliente, Raza


class ControladorMascota:
    def __init__(self):
        self.vista = VistaMascota()
        self.listamascotas = []
        self.cargarmascota()

    def agregarmascota(self, listarazas: list[Raza], listaclientes: list[Cliente]):
        nrocliente, nroraza = self.vista.solicitarnro_cliente(), self.vista.solicitarnro_raza()
        for cliente in listaclientes:
            if cliente.nro == nrocliente:
                for raza in listarazas:
                    if raza.nro == nroraza:
                        self.listamascotas.append(
                            Mascota(self.vista.solicitarnro(), self.vista.solicitarnombre(), self.vista.solicitarfechanacimiento(),
                                    nrocliente, nroraza))
                        self.listamascotas[-1].dar_alta()
                        self.vista.mostrarmensaje(1)

    def modificarmascotas(self, listarazas: list[Raza], listaclientes: list[Cliente]):
        self.vista.mostrarListaMascota(self.listamascotas)
        self.vista.mostrarmensaje(2)
        nromascotas = self.vista.solicitarnro()
        for mascota in self.listamascotas:
            if mascota.nro == nromascotas:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                if cambio in ("4", "5"):
                    for cliente in listaclientes:
                        if cliente.nro == nuevo_valor:
                            mascota.modificar_datos(cambio, nuevo_valor)
                    for raza in listarazas:
                        if raza.nro == nuevo_valor:
                            mascota.modificar_datos(cambio, nuevo_valor)
                mascota.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminarmascota(self):
        self.vista.mostrarListaMascota(self.listamascotas)
        self.vista.mostrarmensaje(5)
        nromascota = self.vista.solicitarnombre()
        for mascota in self.listamascotas:
            if mascota.nro == nromascota:
                self.listamascotas[self.listamascotas.index(mascota)].dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def cargarmascota(self):
        try:
            file = open("Txt/mascotas.txt",encoding='utf-8')
            for line in file:
                var1 = line.strip().split(",")
                self.listamascotas.append(Mascota(int(var1[0]), var1[1], var1[2], int(var1[3]), int(var1[4]), int(var1[5])))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarmascota(self):
        guardado = ""
        for mascota in self.listamascotas:
            guardado += f"{mascota}\n"
        file = open("Txt/mascotas.txt", "r+")
        file.write(guardado[0:-1])
        file.close()

    def ver_lista_mascotas(self):
        self.vista.mostrarListaMascota(self.listamascotas)


    def calcularconsultaxmascota(self,listaconsulta: list[Consulta]):
        nromascota = self.vista.solicitarnro()
        acu = 0
        for consulta in listaconsulta:
            if consulta.nro == nromascota:
                acu += 1
        for mascota in self.listamascotas:
                if mascota.nro == nromascota:
                    self.vista.mostrarnroconsultaxmascota(self.listamascotas[self.listamascotas.index(mascota)].nombre,acu)
