from src.estudiantes.domain.crear import CrearEstudiantes

class CrearEstudiantesCase:
    def __init__(self, db, estudiantesModel, estudiantesDTO):
        self.db=db
        self.estudiantesModel=estudiantesModel
        self.estudiantesDTO=estudiantesDTO

    def run(self):
        crearEstudiantes=CrearEstudiantes(self.db, self.estudiantesModel, self.estudiantesDTO)
        return crearEstudiantes.run()
