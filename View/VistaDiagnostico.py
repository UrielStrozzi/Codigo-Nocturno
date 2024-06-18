class VistaDiagnostico:
    def solicitarcodigo(self):
        return input("Ingrese el codigo del diagnostico: ")
    def solicitartipo(self):
        return input("Ingrese el tipo de diagnóstico (leve, moderado, severo, grave): ")

    def solicitardescripcion(self):
        return input("ingrese la descripcion de la diagnostico: ")

    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Diagnostico creada con exito")
        elif numero == 2:
            print("Que Diagnostico quiere modificar: ")
        elif numero == 3:
            print("Diagnostico modificada con éxito")
        elif numero == 4:
            print("La Diagnostico especificada no fue encontrada")
        elif numero == 5:
            print("¿Que Diagnostico desea eliminar?")
        elif numero == 6:
            print("Diagnostico deshabilitada con exito!")
        elif numero == 7:
            print("Diagnostico no encontrada")
        elif numero == 8:
            print("Archivo de Diagnostico no encontrado")

    def mostrardiagnostico(self, lista):
        for diagnostico in lista:
            print(diagnostico)

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Codigo\n2-Tipo\n3-Descripcion")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")

