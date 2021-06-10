class ListarSemestres():
    def __init__(self, semestresModel):
        self.semestresModel=semestresModel

    def run(self):
        return [self.semestresModel.json(user) for user in self.semestresModel.query.all()]