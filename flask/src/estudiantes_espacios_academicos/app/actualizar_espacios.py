from src.espacios_academicos.domain.actualizar import ActualizarEspacio

class ActualizarEspacioCase:
    def __init__(self,db,espacioModel, espaciosDTO, _id):
        self.db=db
        self.espacioModel=espacioModel
        self.espaciosDTO=espaciosDTO
        self._id=_id

    def run(self):
        actualizarEspacio=ActualizarEspacio(self.db,self.espacioModel,self.espaciosDTO, self._id)
        return actualizarEspacio.run()