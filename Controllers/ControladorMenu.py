from View.VistaMenu import VistaMenu
from Controllers.ControladorRaza import ControladorRaza
from Controllers.ControladorVacuna import ControladorVacuna
from Controllers.ControladorTratamiento import ControladorTratamiento
from Controllers.ControladorDiagonostico import ControladorDiagnostico
class ControladorMenu:
    def __init__(self):
        self.vista = VistaMenu()
        self.controldorraza = ControladorRaza()
        self.controladorvacuna = ControladorVacuna()
        self.controladordiagnostico = ControladorDiagnostico()
        self.controladortratamiento = ControladorTratamiento()

    def iniciar(self):
        menu = -1
        while menu != 0:
            self.vista.mostraropciones()
            menu = self.vista.solicitaropcion()
            if menu == 0:
                self.vista.mostrarmensaje(0)

            elif menu == 2:
                self.controladortratamiento.ver_lista_tratamiento()

            elif menu == 3:
                self.controladordiagnostico.ver_lista_diagnostico()

            elif menu == 4:
                self.controladorvacuna.ver_lista_vacuna()

            elif menu == 5:
                self.controldorraza.ver_lista_razas()

            elif menu == 13:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controldorraza.agregarraza()
                elif menu == 2:
                    self.controldorraza.modificarraza()
                elif menu == 3:
                    self.controldorraza.eliminarraza()
                self.controldorraza.guardarrazas()
            elif menu == 16:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controladordiagnostico.agregardiagnostico()
                elif menu == 2:
                    self.controladordiagnostico.modificardiagnostico()
                elif menu == 3:
                    self.controladordiagnostico.eliminardiagnostico()
                self.controladordiagnostico.guardardiagnostico()

            elif menu == 17:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controladortratamiento.agregartratamiento()
                elif menu == 2:
                    self.controladortratamiento.modificartratamiento()
                elif menu == 3:
                    self.controladortratamiento.eliminartratamiento()
                self.controladortratamiento.guardartratamiento()
            elif menu == 19:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controladorvacuna.agregarvacuna()
                elif menu == 2:
                    self.controladorvacuna.modificarvacuna()
                elif menu == 3:
                    self.controladorvacuna.eliminarvacuna()


            """elif menu == 1:
                ver_lista_mascotas_activas()
            
            elif menu == 3:
                ver_lista_diagnostico()
            
            
            elif menu == 6:
                ver_lista_veterinarios()
            elif menu == 7:
                ver_lista_clientes()
            elif menu == 8:
                calcularCantMascXCliente()
            elif menu == 9:
                calcularCantConsulXMascot()
            elif menu == 10:
                calcular_tratam_aplicados()
            elif menu == 11:
                calcularRankingDiagnos()
            elif menu == 12:
                calcularCantRazasXDiagnos()
            # OPCIONES DEL PROGRAMADOR y VETERINARIOS
            elif menu == 13:
                gestionar_razas()
            elif menu == 14:
                gestionar_mascotas()
            elif menu == 15:
                gestionar_personas()
            
    
            elif menu == 18:
                gestionar_fichas_medicas()"""
            """else:
                print("Ingrese una opción correcta.")"""