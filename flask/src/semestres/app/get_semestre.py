from src.semestres.domain.get import GetSemestre 

class GetSemestreCase:
    def __init__(self,_id, semestresModel):
        self.semestresModel=semestresModel
        self._id=_id

    def run(self):
        getSemestre=GetSemestre(self._id, self.semestresModel)
        return getSemestre.run()
    def run_native(self):
        getSemestre=GetSemestre(self._id, self.semestresModel)
        return getSemestre.run_native()
