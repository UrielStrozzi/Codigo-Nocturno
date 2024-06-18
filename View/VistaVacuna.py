class VistaVacuna:

    def mostrarvacunas(self, lista):
        for vacuna in lista:
            print(vacuna)
    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Vacuna agregada con exito.")
        elif numero == 2:
            print("Que vacuna quiere modificar: ")
        elif numero == 3:
            print("Vacuna modificada con éxito")
        elif numero == 5:
            print("¿Que vacuna desea eliminar?")
        elif numero == 6:
            print("vacuna deshabilitada con exito!")
        elif numero == 7:
            print("vacuna no encontrada")
        elif numero == 8:
            print("Archivo de razas no encontrado")

    def solicitarnombre(self):
        return input("ingrese el nombre de la vacuna: ")

    def solicitartipo(self):
        return input("ingrese el tipo de la vacuna: ")

    def solicitarprecio(self):
        return input("ingrese el precio: ")

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Nombre\n2-Tipo\n3-Precio")
        return input()

    def solicitarvalorcambio(self):
        print("Ingrese el valor del cambio: ")
