class VistaMascota:
    def mostrarListaMascota(self, lista):
        for mascota in lista:
            print(mascota)

    def solicitarnro(self):
        return int(input("ingrese el numero de la mascota: "))

    def solicitarnombre(self):
        return input("ingrese el nombre de la mascotas: ")

    def solicitarfechanacimiento(self):
        return input("ingrese la fecha de nacimiento: ")

    def solicitarcliente(self):
        return input("ingrese el nombre del cliente: ")

    def solicitaraza(self):
        return input("ingrese la raza de la mascota: ")

    def solicitarnro_cliente(self):
        return int(input("ingrese el nro del cliente: "))

    def solicitarnro_raza(self):
        return int(input("ingrese la raza: "))

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

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Numero\n2-Nombre\n3-Color\n4-Tamano\n5-Pelaje")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")

    def mostrarnroconsultaxmascota(self, nombremascota, acu):
        print(f"El numero de consultas que tiene {nombremascota} es: {acu}")