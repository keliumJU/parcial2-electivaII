from src.asistencia.domain.listar import ListarFaltantes 

class ListarFaltantesCase:
    def __init__(self, faltantesDTO, get_estudiante, estudiantesModel):
        self.faltantesDTO=faltantesDTO
        self.get_estudiante=get_estudiante
        self.estudiantesModel=estudiantesModel

    def run(self):
        listarFaltantes = ListarFaltantes(self.faltantesDTO, self.get_estudiante, self.estudiantesModel)
        return listarFaltantes.run()