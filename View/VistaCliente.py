class VistaCliente:

    def solicitarnro(self):
        return int(input("Ingrese numero del cliente: "))

    def solicitarnombre(self):
        return input("ingrese el nombre del cliente: ")

    def solicitarapellido(self):
        return input("ingrese el apellido del cliente: ")

    def solicitardireccion(self):
        return input("ingrese la direccion del cliente: ")

    def solicitartelefono(self):
        return input("ingrese el telefono del cliente: ")

    def mostrarmensaje(self, numero):
        if numero == 1:
            print("Cliente creado con exito")
        elif numero == 2:
            print("Que cliente quiere modificar: ")
        elif numero == 3:
            print("Cliente modificado con éxito")
        elif numero == 4:
            print("El cliente especificado no fue encontrado")
        elif numero == 5:
            print("¿Que cliente desea eliminar?")
        elif numero == 6:
            print("Cliente deshabilitado con exito!")
        elif numero == 7:
            print("Cliente no encontrado")
        elif numero == 8:
            print("Archivo de clientes no encontrado")

    def mostrarcliente(self, lista):
        for cliente in lista:
            print(cliente)

    def mostrarnromascotasporcliente(self, nombrecliente, acu):
        print(f"El numero de masotas que tiene {nombrecliente} es: {acu}")

    def solicitarcambio(self):
        print("Dato a modificar: \n1-Numero\n2-Nombre\n3-Apellido\n4-Direccion\n5-Telefono")
        return input()

    def solicitarvalorcambio(self):
        return input("Ingrese el valor del cambio: ")
