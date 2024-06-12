class VistaMascota:
    def mostrarListaMascota(self,lista):
        for mascota in lista:
            print(mascota)

    def solicitarnombre(self):
        return input("ingrese el nombre de la raza: ")

    def solicitarfechanacimietno(self):
        return input("ingrese la fecha de nacimiento: ")
    def solicitarcliente(self):
        return input("ingrese el nombre del cliente: ")

    def solicitaraza(self):
        return input("ingrese la raza: ")

    def solicitarfichamedica(self):
        return input("ingrese la ficha medica: ")

    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Raza creada con exito.")