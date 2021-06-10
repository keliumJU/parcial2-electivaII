from src.semestres.domain.listar import ListarSemestres

class ListarSemestresCase:
    def __init__(self,semestresModel):
        self.semestresModel=semestresModel

    def run(self):
        listarSemestres=ListarSemestres(self.semestresModel)
        return listarSemestres.run()