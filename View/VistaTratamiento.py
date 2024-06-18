class VistaTratamiento:

    def solicitarcodigo(self):
        return input("Ingrese el codigo: ")

    def solicitartipo(self):
        return input("ingrese el tipo del traramiento: ")

    def solicitardetalle(self):
        return input("ingrese la descripcion del tratamiento: ")

    def mostrarmensaje(self, numero):
        if numero == 1:
            print("tratamiento creada con exito")
        elif numero == 2:
            print("Que tratamiento quiere modificar: ")
        elif numero == 3:
            print("tratamiento modificada con éxito")
        elif numero == 4:
            print("La tratamiento especificada no fue encontrada")
        elif numero == 5:
            print("¿Que tratamiento desea eliminar?")
        elif numero == 6:
            print("tratamiento deshabilitada con exito!")
        elif numero == 7:
            print("tratamiento no encontrada")
        elif numero == 8:
            print("Archivo de tratamiento no encontrado")

    def mostrartratamiento(self, lista):
        for tratamiento in lista:
            print(tratamiento)

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Codigo\n2-Tipo\n3-Descripcion")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")
