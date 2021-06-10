from src.estudiantes.domain.actualizar import ActualizarEstudiantes

class ActualizarEstudiantesCase:
    def __init__(self, db, estudiantesModel, estudiantesDTO):
        self.db=db
        self.estudiantesModel=estudiantesModel
        self.estudiantesDTO=estudiantesDTO
    def run(self):
        actualizarEstudiantes=ActualizarEstudiantes(self.db,self.estudiantesModel,self.estudiantesDTO)
        return actualizarEstudiantes.run()