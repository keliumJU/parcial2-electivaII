from src.shared.infra.Modelos import Estudiantes,Sesiones


class AsistenciaDTO():
    estudiante:Estudiantes
    sesion:Sesiones

    def __init__(self,estudiante,sesion):
        self.estudiante=estudiante
        self.sesion=sesion