class VistaMenu:
    def mostrarmensaje(self, menu):
        if menu == 0:
            print("Cerrando programa")
        elif menu == 1:
            print("Ver lista de mascotas activas")
        elif menu == 2:
            print("Ver lista de tratamientos")
        elif menu == 3:
            print("Ver lista de diagnósticos")
        elif menu == 4:
            print("Ver lista de vacunas")
        elif menu == 5:
            print("Ver lista de razas")
        elif menu == 6:
            print("Ver lista de veterinarios")
        elif menu == 7:
            print("Ver lista de clientes")
        elif menu == 8:
            print("Calcular cantidad de mascotas por cliente")
        elif menu == 9:
            print("Calcular cantidad de consultas por mascota")
        elif menu == 10:
            print("Calcular tratamientos aplicados")
        elif menu == 11:
            print("Calcular ranking de diagnósticos")
        elif menu == 12:
            print("Calcular cantidad de razas por diagnóstico")
        elif menu == 13:
            print("Gestionar razas\n1-Agregar Raza-\n2-Modificar Raza.\n3-Dar de baja raza.")
        elif menu == 14:
            print("Gestionar mascotas\n1-Agregar mascotas-\n2-Modificar mascotas.\n3-Dar de baja mascotas.")
        elif menu == 15:
            print("Gestionar clientes\n1-Agregar cliente-\n2-Modificar cliente.\n3-Dar de baja cliente.")
        elif menu == 16:
            print("Gestionar Diagnostico\n1-Agregar Diagnostico\n2-Modificar Diagnostico.\n3-Dar de baja Diagnostico.")
        elif menu == 17:
            print("Gestionar Tratamientos\n1-Agregar Tratamiento-\n2-Modificar Tratamiento.\n3-Dar de baja Tratamiento.")
        elif menu == 18:
            print("Gestionar vacuna\n1-Agregar vacuna\n2-Modificar vacuna\n3-Dar de baja vacuna")
        elif menu == 19:
            print("Gestionar Ficha Medica\n1-Agregar Ficha Medica\n2-Modificar Ficha Medica\n3-Dar de baja Ficha Medica")
        elif menu == 20:
            print("Gestionar consulta\n1-Agregar Consulta\n2-Modificar Consulta\n3-Cerrar Consulta")
        else:
            print("Ingrese una opción correcta.")

    def solicitaropcion(self):
        return int(input("Ingrese la opcion: "))

    def mostraropciones(self):
        print("1- Ver lista de mascotas activas\n"
              "2- Ver lista de tratamientos\n"
              "3- Ver lista de diagnósticos\n"
              "4- Ver lista de vacunas\n"
              "5- Ver lista de razas\n"
              "6- Ver lista de veterinarios\n"
              "7- Ver lista de clientes\n"
              "8- Calcular cantidad de mascotas por cliente\n"
              "9- Calcular cantidad de consultas por mascota\n"
              "10- Calcular tratamientos aplicados\n"
              "11- Calcular ranking de diagnósticos\n"
              "12- Calcular cantidad de razas por diagnóstico\n"
              "13- Gestionar razas\n"
              "14- Gestionar mascotas\n"
              "15- Gestionar personas\n"
              "16- Gestionar diagnósticos\n"
              "17- Gestionar tratamientos\n"
              "18- Gestionar vacunas\n"
              "19- Gestionar fichas médicas"
              "\n20- Gestionar consultas\n"
              "0- Salir del programa")
