from View.VistaCliente import VistaCliente
from Models.Cliente import Cliente
from Models.Mascota import Mascota


class ControladorCliente:
    def __init__(self):
        self.vista = VistaCliente()
        self.listacliente: list[Cliente] = []

    def agregarcliente(self):
        self.listacliente.append(Cliente(self.vista.solicitarnro(), self.vista.solicitarnombre(),
                                         self.vista.solicitarapellido(), self.vista.solicitardireccion(),
                                         self.vista.solicitartelefono(),))
        self.listacliente[-1].dar_alta()
        self.vista.mostrarmensaje(1)

    def modificarcliente(self):
        self.vista.mostrarcliente(self.listacliente)
        self.vista.mostrarmensaje(2)
        nrocliente = self.vista.solicitarnro()
        for cliente in self.listacliente:
            if cliente.nro == nrocliente:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                cliente.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminarcliente(self):
        self.vista.mostrarcliente(self.listacliente)
        self.vista.mostrarmensaje(5)
        nrocliente = self.vista.solicitarnro()
        for cliente in self.listacliente:
            if cliente.nro == nrocliente:
                self.listacliente[self.listacliente.index(cliente)].dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def cargarclientes(self):
        try:
            file = open("Txt/cliente.txt",encoding='utf-8')
            for line in file:
                var1 = line.strip().split(",")
                self.listacliente.append(Cliente(int(var1[0]), var1[1], var1[2], var1[3], int(var1[4]), int(var1[5])))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarcliente(self):
        guardado = ""
        for cliente in self.listacliente:
            guardado += f"{cliente}\n"
        file = open("Txt/cliente.txt", "r+")
        file.write(guardado[0:-1])
        file.close()

    def ver_lista_clientes(self):
        self.vista.mostrarcliente(self.listacliente)

    def calcular_cantidad_mascotasxcliente(self, listamascotas: list[Mascota]):
        nrocliente = self.vista.solicitarnro()
        acu = 0
        for mascota in listamascotas:
            if mascota.nrocliente == nrocliente:
                acu += 1
        for cliente in self.listacliente:
            if cliente.nro == nrocliente:
                self.vista.mostrarnromascotasporcliente(self.listacliente[self.listacliente.index(cliente)].nombre, acu)
