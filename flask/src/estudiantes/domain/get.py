class GetEstudiante():
    def __init__(self, estudiantesModel, id_):
        self.estudiantesModel=estudiantesModel
        self.id_=id_

    def run(self):
        estudiante=self.estudiantesModel.query.filter_by(identificacion=self.id_).first()
        return self.estudiantesModel.json(estudiante)
    
    def run_native(self):
        return self.estudiantesModel.query.filter_by(identificacion=self.id_).first()