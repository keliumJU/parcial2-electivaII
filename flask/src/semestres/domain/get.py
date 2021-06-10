class GetSemestre():
    def __init__(self, id_, semestresModel):
        self.semestresModel=semestresModel
        self.id_=id_

    def run(self):
        semestre = self.semestresModel.query.filter_by(semestre_id=self.id_).first()
        return self.semestresModel.json(semestre)
    
    def run_native(self):
        semestre = self.semestresModel.query.filter_by(semestre_id=self.id_).first()
        return semestre
        