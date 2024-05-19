# OPCIONES DEL PROGRAMADOR y VETERINARIOS
def gestionar_fichas_medicas():
    print("Gestionar fichas médicas")


def gestionar_tratamientos():
    print("Gestionar tratamientos")


def gestionar_diagnosticos():
    print("Gestionar diagnósticos")


def gestionar_personas():
    print("Gestionar personas")


def gestionar_mascotas():
    print("Gestionar mascotas")


def gestionar_razas():
    print("Gestionar razas")


# OPCIONES DE CLIENTES Y VETERINARIOS
def calcularCantRazasXDiagnos():
    print("Calcular cantidad de razas por diagnóstico")


def calcularRankingDiagnos():
    print("Calcular ranking de diagnósticos")


def calcular_tratam_aplicados():
    print("Calcular tratamientos aplicados")


def calcularCantConsulXMascot():
    print("Calcular cantidad de consultas por mascota")


def calcularCantMascXCliente():
    print("Calcular cantidad de mascotas por cliente")


def ver_lista_clientes():
    print("Ver lista de clientes")


def ver_lista_veterinarios():
    print("Ver lista de veterinarios")


def ver_lista_razas():
    print("Ver lista de razas")


def ver_lista_vacunas():
    print("Ver lista de vacunas")


def ver_lista_diagnostico():
    print("Ver lista de diagnósticos")


def ver_lista_tratamientos():
    print("Ver lista de tratamientos")


def ver_lista_mascotas_activas():
    print("Ver lista de mascotas activas")


def main():
    opciones = """
    OPCIONES DE CLIENTES Y VETERINARIOS:
    1- Ver lista de mascotas activas
    2- Ver lista de tratamientos
    3- Ver lista de diagnósticos
    4- Ver lista de vacunas
    5- Ver lista de razas
    6- Ver lista de veterinarios
    7- Ver lista de clientes
    8- Calcular cantidad de mascotas por cliente
    9- Calcular cantidad de consultas por mascota
    10- Calcular tratamientos aplicados
    11- Calcular ranking de diagnósticos
    12- Calcular cantidad de razas por diagnóstico

    OPCIONES DEL PROGRAMADOR y VETERINARIOS:
    13- Gestionar razas
    14- Gestionar mascotas
    15- Gestionar personas
    16- Gestionar diagnósticos
    17- Gestionar tratamientos
    18- Gestionar fichas médicas
    """
    try:
        while True:
            print(opciones)
            opcion = int(input("Ingrese el número de la opción que desea realizar: "))

            # OPCIONES DE CLIENTES Y VETERINARIOS
            if opcion == 1:
                ver_lista_mascotas_activas()
            elif opcion == 2:
                ver_lista_tratamientos()
            elif opcion == 3:
                ver_lista_diagnostico()
            elif opcion == 4:
                ver_lista_vacunas()
            elif opcion == 5:
                ver_lista_razas()
            elif opcion == 6:
                ver_lista_veterinarios()
            elif opcion == 7:
                ver_lista_clientes()
            elif opcion == 8:
                calcularCantMascXCliente()
            elif opcion == 9:
                calcularCantConsulXMascot()
            elif opcion == 10:
                calcular_tratam_aplicados()
            elif opcion == 11:
                calcularRankingDiagnos()
            elif opcion == 12:
                calcularCantRazasXDiagnos()

            # OPCIONES DEL PROGRAMADOR y VETERINARIOS
            elif opcion == 13:
                gestionar_razas()
            elif opcion == 14:
                gestionar_mascotas()
            elif opcion == 15:
                gestionar_personas()
            elif opcion == 16:
                gestionar_diagnosticos()
            elif opcion == 17:
                gestionar_tratamientos()
            elif opcion == 18:
                gestionar_fichas_medicas()
            else:
                print("Ingrese una opción correcta.")

    except ValueError:
        print("Error. Intente nuevamente")


if __name__ == "__main__":
    main()
