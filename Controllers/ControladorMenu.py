from View.VistaMenu import VistaMenu
from Controllers.ControladorRaza import ControladorRaza
from Controllers.ControladorVacuna import ControladorVacuna
from Controllers.ControladorTratamiento import ControladorTratamiento
from Controllers.ControladorDiagonostico import ControladorDiagnostico
from Controllers.ControladorCliente import ControladorCliente
from Controllers.ControladorConsulta import ControladorConsulta
from Controllers.ControladorMascota import ControladorMascota
from Controllers.ControladorVeterinario import ControladorVeterinario
from Controllers.ControladorFichamedica import ControladorFichaMedica

class ControladorMenu:
    def __init__(self):
        self.vista = VistaMenu()
        self.controldorraza = ControladorRaza()
        self.controladorvacuna = ControladorVacuna()
        self.controladordiagnostico = ControladorDiagnostico()
        self.controladortratamiento = ControladorTratamiento()
        self.controladorcliente = ControladorCliente()
        self.controladormascota = ControladorMascota()
        self.controladorveterinario = ControladorVeterinario()
        self.controladorconsulta = ControladorConsulta()
        self.controladorfichamedica = ControladorFichaMedica()

    def iniciar(self):
        menu = -1
        while menu != 0:
            self.vista.mostraropciones()
            menu = self.vista.solicitaropcion()
            if menu == 0:
                self.vista.mostrarmensaje(0)
            elif menu == 1:
                self.controladormascota.ver_lista_mascotas()
            elif menu == 2:
                self.controladortratamiento.ver_lista_tratamientos()
            elif menu == 3:
                self.controladordiagnostico.ver_lista_diagnosticos()
            elif menu == 4:
                self.controladorvacuna.ver_lista_vacunas()
            elif menu == 5:
                self.controldorraza.ver_lista_razas()
            elif menu == 6:
                self.controladorveterinario.ver_lista_veterinario()
            elif menu == 7:
                self.controladorcliente.ver_lista_clientes()
            elif menu == 8:
                self.controladorcliente.calcular_cantidad_mascotasxcliente(self.controladormascota.listamascotas)
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
            elif menu == 14:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controladormascota.agregarmascota(self.controldorraza.listarazas,
                                                           self.controladorcliente.listacliente)
                elif menu == 2:
                    self.controladormascota.modificarmascotas(self.controldorraza.listarazas,
                                                              self.controladorcliente.listacliente)
                elif menu == 3:
                    self.controladormascota.eliminarmascota()
                self.controladormascota.guardarmascota()
            elif menu == 15:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controladorcliente.agregarcliente()
                elif menu == 2:
                    self.controladorcliente.modificarcliente()
                elif menu == 3:
                    self.controladorcliente.eliminarcliente()
                self.controladorcliente.guardarcliente()
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
            elif menu == 18:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                if menu == 1:
                    self.controladorvacuna.agregarvacuna()
                elif menu == 2:
                    self.controladorvacuna.modificarvacuna()
                elif menu == 3:
                    self.controladorvacuna.eliminarvacuna()
            elif menu == 19:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                ficha,t, consulta = self.controladorfichamedica.listafichamedica,self.controladortratamiento.listatratamiento, self.controladorconsulta.listaconsulta
                if menu == 1:
                    self.controladorfichamedica.agregarfichamedica(ficha,t, consulta)
                elif menu == 2:
                    self.controladorfichamedica.modificarfichamedica(ficha,t, consulta)
                elif menu == 3:
                    self.controladorfichamedica.eliminarfichamedica()

            elif menu == 20:
                self.vista.mostrarmensaje(menu)
                menu = self.vista.solicitaropcion()
                c, v, t, d, vac = self.controladorcliente.listacliente, self.controladorveterinario.listaveterinario, self.controladordiagnostico.listadiagnostico, self.controladortratamiento.listatratamiento, self.controladorvacuna.listavacunas
                if menu == 1:
                    self.controladorconsulta.agregarconsulta(c, v, d, t, vac)
                elif menu == 2:
                    self.controladorconsulta.modificarconsulta(c, v, d, t, vac)
                elif menu == 3:
                    self.controladorconsulta.eliminarconsulta()
            else:
                self.vista.mostrarmensaje(menu)

            """
            elif menu == 9:
                calcularCantConsulXMascot()
            elif menu == 10:
                calcular_tratam_aplicados()
            elif menu == 11:
                calcularRankingDiagnos()
            elif menu == 12:
                calcularCantRazasXDiagnos()
            elif menu == 18:
                gestionar_fichas_medicas()
            """
