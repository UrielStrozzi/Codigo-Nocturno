class VistaConsulta:
    def solicitarnro(self):
        return int(input("ingrese el nro de la consula: "))

    def solicitarobservacion(self):
        return input("ingrese la observaciones de la consulta: ")

    def solicitarcliente(self):
        return int(input("ingrese el numero del cliente: "))

    def solicitarveterinario(self):
        return int(input("ingrese la matricula del veterinario: "))

    def solicitartratamiento(self):
        return int(input("ingrese el numero de tratamiento: "))

    def solicitardiagnostico(self):
        return int(input("ingrese el numero diagnostico: "))

    def solicitarvacuna(self):
        return int(input("ingrese el pelaje de la raza: "))

    def solicitarfecha(self):
        return (input("ingrese la fecha de la consulta: "))


    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Consulta creada con exito")
        elif numero == 2:
            print("Que consulta quiere modificar: ")
        elif numero == 3:
            print("Consulta modificada con éxito")
        elif numero == 4:
            print("La consulta especificada no fue encontrada")
        elif numero == 5:
            print("¿Que consulta desea eliminar?")
        elif numero == 6:
            print("Consulta deshabilitada con exito!")
        elif numero == 7:
            print("Consulta no encontrada")
        elif numero == 8:
            print("Archivo de consultas no encontrado")
        elif numero == 10:
            print("Opcion no valida")

    def solicitaranadiroquitar(self):
        return input("\nSi desea borrar dicho valor, ingrese 1"
                     "\nDe lo contrario, ingrese 0")

    def solicitaropcion(self):
        return int(input("1-Agregar Veterinario."
                         "\n2-Agregar un diagnostico"
                         "\nSi desea agregar un tratamiento escriba 3"
                         "\nSi desea agregar una vacuna escriba 4"
                         "\nDe lo contrario, escriba 0"))

    def mostrarconsulta(self, lista):
        for raza in lista:
            print(raza)

    def solicitarcambio(self):
        print("\nDato a modificar: \n1-Nro\n2-Observaciones\n3-Fecha\n4-Cliente"
              "\n5-Veterinarios\n6-Diagnostico\n7-tratamientos"
              "\n8-Vacunas")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")
