class ListarEstudiantes():
    def __init__(self, estudiantesModel):
        self.estudiantesModel=estudiantesModel

    def run(self):
        return [self.estudiantesModel.json(user) for user in self.estudiantesModel.query.all()]