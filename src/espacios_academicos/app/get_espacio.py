from src.espacios_academicos.domain.get import GetEspacio

class GetEspacioCase:
    def __init__(self,espacioModel, _id):
        self.espacioModel=espacioModel
        self._id=_id

    def run(self):
        getEspacio= GetEspacio(self.espacioModel, self._id)
        return getEspacio.run()
    
    def run_native(self):
        getEspacio= GetEspacio(self.espacioModel, self._id)
        return getEspacio.run_native()   