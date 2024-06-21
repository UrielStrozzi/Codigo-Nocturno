class VistaVeterinario:

    def solicitarnro_matricula(self):
        return int(input("Ingrese numero del cliente: "))

    def solicitarnombre(self):
        return input("ingrese el nombre de la raza: ")
    def solicitarapellido(self):
        return input("ingrese el apellido de la raza: ")
    def solicitardireccion(self):
        return input("ingrese la direccion de la raza: ")
    def solicitartelefono(self):
        return input("ingrese el telefono de la raza: ")
    def solicitarespecializacion(self):
        return input("ingrese el especializacion de la raza: ")

    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Raza creada con exito")
        elif numero == 2:
            print("Que raza quiere modificar: ")
        elif numero == 3:
            print("Raza modificada con éxito")
        elif numero == 4:
            print("La raza especificada no fue encontrada")
        elif numero == 5:
            print("¿Que raza desea eliminar?")
        elif numero == 6:
            print("Raza deshabilitada con exito!")
        elif numero == 7:
            print("Raza no encontrada")
        elif numero == 8:
            print("Archivo de razas no encontrado")

    def mostrarveterinario(self, lista):
        for cliente in lista:
            print(cliente)

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Numero\n2-Nombre\n3-Apellido\n4-Direccion\n5-Telefono")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")

