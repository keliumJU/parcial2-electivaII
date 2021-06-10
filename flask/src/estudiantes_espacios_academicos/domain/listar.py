class ListarEspaciosAcademicos():
    def __init__(self, espaciosAcademicosModel):
        self.espaciosAcademicosModel=espaciosAcademicosModel

    def run(self):
        return [self.espaciosAcademicosModel.json(espa) for espa in self.espaciosAcademicosModel.query.all()]