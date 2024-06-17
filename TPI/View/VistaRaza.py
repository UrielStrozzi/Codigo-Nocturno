class VistaRaza:
    def solicitarnombre(self):
        return input("ingrese el nombre de la raza: ")

    def solicitarnro(self):
        return int(input("ingrese el nro de la raza: "))

    def solicitarcolor(self):
        return input("ingrese el color de la raza: ")

    def solicitartamano(self):
        return input("ingrese el tamano de la raza: ")

    def solicitarpelaje(self):
        return input("ingrese el pelaje de la raza: ")

    def mostrarmensaje(self,numero):
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

    def mostrarraza(self, lista):
        for raza in lista:
            print(raza)

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Nombre\n2-Color\n3-Tamano\n4-Pelaje")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")

