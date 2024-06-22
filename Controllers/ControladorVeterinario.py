from View.VistaVeterinario import VistaVeterinario
from Models.Veterinario import Veterinario


class ControladorVeterinario:
    def __init__(self):
        self.vista = VistaVeterinario()
        self.listaveterinario: list[Veterinario] = []
        self.cargarveterinario()

    def agregarveterinario(self):
        self.listaveterinario.append(Veterinario(self.vista.solicitarnro_matricula(), self.vista.solicitarnombre(),
                                                 self.vista.solicitarapellido(), self.vista.solicitardireccion(),
                                                 self.vista.solicitartelefono(), self.vista.solicitarespecializacion()))
        self.listaveterinario[-1].dar_alta()
        self.vista.mostrarmensaje(1)

    def modificarveterianrio(self):
        self.vista.mostrarveterinario(self.listaveterinario)
        self.vista.mostrarmensaje(2)
        nromatricula = self.vista.solicitarnro_matricula()
        for veterinario in self.listaveterinario:
            if veterinario.nro_matricula == nromatricula:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                veterinario.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminarveterinario(self):
        self.vista.mostrarveterinario(self.listaveterinario)
        self.vista.mostrarmensaje(5)
        nromatricula = self.vista.solicitarnro_matricula()
        for veterinario in self.listaveterinario:
            if veterinario.nro == nromatricula:
                self.listaveterinario[self.listaveterinario.index(veterinario)].dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def cargarveterinario(self):
        try:
            file = open("Txt/veterinario.txt",encoding='utf-8')
            for line in file:
                var1 = line.strip().split(",")
                self.listaveterinario.append(
                    Veterinario(int(var1[0]), var1[1], var1[2], var1[3], int(var1[4]), var1[5], int(var1[6])))
            file.close()
        except FileExistsError or FileNotFoundError:
            self.vista.mostrarmensaje(8)

    def guardarveterinario(self):
        guardado = ""
        for cliente in self.listaveterinario:
            guardado += f"{cliente}\n"
        file = open("Txt/veterinario.txt", "r+")
        file.write(guardado[0:-1])
        file.close()

    def ver_lista_veterinario(self):
        self.vista.mostrarveterinario(self.listaveterinario)
