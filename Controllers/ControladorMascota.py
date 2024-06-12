from ..View.VistaMascota import VistaMascota
from ..Models.Mascota import Mascota
class ControladorMascota:
    def __init__(self):
        self.visa = VistaMascota()
        self.listamascotas =  []

    def agregarmascota(self):
        self.listarazas.append(
            Mascota(self.vista.solicitarnombre(), self.vista.solicitarfechanacimietno(), self.visa.solicitarcliente(),self.vista.solicitaraza(),
                    self.vista.solicitarfichamedica()))
        self.listamascotas[-1].dar_alta()
        self.vista.mostrarmensaje(1)

