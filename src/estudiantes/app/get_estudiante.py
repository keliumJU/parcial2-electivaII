from src.estudiantes.domain.get import GetEstudiante 

class GetEstudianteCase:
    def __init__(self,estudiantesModel, _id):
        self.estudiantesModel=estudiantesModel
        self._id=_id

    def run(self):
        getEstudiante= GetEstudiante(self.estudiantesModel, self._id)
        return getEstudiante.run()
    
    def run_native(self):
        getEstudiante= GetEstudiante(self.estudiantesModel, self._id)
        return getEstudiante.run_native()   