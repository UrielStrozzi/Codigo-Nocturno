class VistaFichaMedica:
    def solicitarnro(self):
        return int(input("ingrese el nro de la ficha medica: "))

    def solicitarobservacion(self):
        return input("Ingrese la observacion: ")

    def solicitartratamiento(self):
        return int(input("ingrese el numero de tratamiento: "))

    def solicitarconsulta(self):
        return int(input("ingrese el numero de consulta: "))



    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Ficha Medica creada con exito")
        elif numero == 2:
            print("Que ficha medica quiere modificar: ")
        elif numero == 3:
            print("Ficha Medica modificada con éxito")
        elif numero == 4:
            print("La Ficha Medica especificada no fue encontrada")
        elif numero == 5:
            print("¿Que Ficha Medica desea eliminar?")
        elif numero == 6:
            print("Ficha Medica deshabilitada con exito!")
        elif numero == 7:
            print("Ficha medica no encontrada")
        elif numero == 8:
            print("Archivo de Ficha Medica no encontrado")
        elif numero == 10:
            print("Opcion no valida")

    def solicitaranadiroquitar(self):
        return input("Si desea borrar dicho valor, ingrese 1"
                     "\nDe lo contrario, ingrese 0")

    def solicitaropcion(self):
        return int(input("1-Agregar Tratamiento\n"
                         "2-Agregar Consulta\n"
                         "0-Salir"))

    def mostrarfichamedica(self, lista):
        for fichamedica in lista:
            print(fichamedica)

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Nro\n2-Observaciones\n3-Fecha\n7-tratamientos\n8-Consulta")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")
