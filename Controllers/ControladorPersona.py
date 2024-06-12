from ..View.VistaMascota import VistaMascota
from ..Models.Mascota import Mascota
class ControladorPersona():
    def __init__(self):
        self.vista = VistaMascota()
        self.listaMascotas = []

    def cagarArchivo(self):
        with open("mascotas.txt") as file:
            renglones = file.readlines()
        for renglon in renglones:
            nombre, fecha_nac, cliente, raza, ficha_medica = renglon.strip().split(";")
            self.listaMascotas.append(Mascota(nombre,fecha_nac,cliente,raza,ficha_medica))
        self.vista.mostrarListaMascota(self.listaMascotas)

    def darAlta(self):
        def darAlta(self, ):
            nueva_mascota = Mascota(self.vista.datosMascotas)

            self.listaMascotas.append(nueva_mascota)
            self.vista.mostrarListaMascota(self.listaMascotas)

