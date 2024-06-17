def main():
    controladorp = ControladorProducto()
    controladorm = ControladorMarca()
    controladorr = ControladorRubro()
    menu = -1
    while menu != "0":
        menu = -1
        print("1 - Listar Productos"
              "0 - Cerrar Programa")
        while menu not in ["0", "1"]:
            menu = input()
            if menu == "1":
                controladorp.listar_productos()
            if menu == "0":
                print("Cerrando programa")

if __name__ == '__main__':
    from Controller.ControladorMarca import ControladorMarca
    from Controller.ControladorProducto import ControladorProducto
    from Controller.ControladorRubro import ControladorRubro
    main()
