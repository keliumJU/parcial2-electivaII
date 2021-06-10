from src.espacios_academicos.domain.listar import ListarEspaciosAcademicos

class ListarEspaciosCase:
    def __init__(self,espaciosAcademicosModel):
        self.espaciosAcademicosModel=espaciosAcademicosModel

    def run(self):
        espaciosAcademicosModel = ListarEspaciosAcademicos(self.espaciosAcademicosModel)
        return espaciosAcademicosModel.run()