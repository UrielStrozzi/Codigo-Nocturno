from Models.Tratamiento import Tratamiento
from View.VistaTratamiento import VistaTratamiento


class ControladorTratamiento:
    def __init__(self):
        self.vista = VistaTratamiento()
        self.listatratamiento: list[Tratamiento] = []
        self.cargartratamiento()

    def agregartratamiento(self):
        tratamiento = Tratamiento(self.vista.solicitarcodigo(), self.vista.solicitartipo(),
                                  self.vista.solicitardetalle())
        tratamiento.dar_alta()
        self.listatratamiento.append(tratamiento)
        self.vista.mostrarmensaje(1)

    def ver_lista_tratamientos(self):
        self.vista.mostrartratamiento(self.listatratamiento)

    def modificartratamiento(self):
        self.vista.mostrartratamiento(self.listatratamiento)
        self.vista.mostrarmensaje(2)
        codigo = self.vista.solicitarcodigo()
        for tratamiento in self.listatratamiento:
            if tratamiento.codigo == codigo:
                cambio = self.vista.solicitarcambio()
                nuevo_valor = self.vista.solicitarvalorcambio()
                tratamiento.modificar_datos(cambio, nuevo_valor)
                self.vista.mostrarmensaje(3)
        self.vista.mostrarmensaje(4)

    def eliminartratamiento(self):
        self.vista.mostrartratamiento(self.listatratamiento)
        self.vista.mostrarmensaje(5)
        codigotratamiento = self.vista.solicitarcodigo()
        for tratamiento in self.listatratamiento:
            if tratamiento.codigo == codigotratamiento:
                tratamiento.dar_baja()
                self.vista.mostrarmensaje(6)
        self.vista.mostrarmensaje(7)

    def cargartratamiento(self):
        try:
            with open("Txt/tratamiento.txt",encoding='utf-8') as file:
                for line in file:
                    var1 = line.strip().split(",")
                    if len(var1) >= 4:  # Asegúrate de que hay suficientes elementos
                        estado = int(var1[3]) if len(var1) > 3 else 0
                        self.listatratamiento.append(Tratamiento(int(var1[0]), var1[1], var1[2], estado))
                    else:
                        print(f"Advertencia: Línea de tratamiento incompleta: {line.strip()}")
        except (FileExistsError, FileNotFoundError):
            self.vista.mostrarmensaje(8)

    def guardartratamiento(self):
        guardado = ""
        for tratamiento in self.listatratamiento:
            guardado += f"{tratamiento}\n"

        with open("Txt/tratamiento.txt", "w") as file:
            file.write(guardado)
