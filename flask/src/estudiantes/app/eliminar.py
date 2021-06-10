from src.estudiantes.domain.eliminar import EliminarEstudiantes

class EliminarEstudiantesCase:
    def __init__(self,db, estudiantesModel, _id):
        self.db=db
        self.estudiantesModel=estudiantesModel
        self._id=_id

    def run(self):
        eliminarEstudiantes=EliminarEstudiantes(self.db, self.estudiantesModel, self._id)
        return eliminarEstudiantes.run()