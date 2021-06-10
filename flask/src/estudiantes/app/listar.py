from src.estudiantes.domain.listar import ListarEstudiantes

class ListarEstudiantesCase:
    def __init__(self,estudiantesModel):
        self.estudiantesModel=estudiantesModel

    def run(self):
        listarEstudiantes = ListarEstudiantes(self.estudiantesModel)
        return listarEstudiantes.run()