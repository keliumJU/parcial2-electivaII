from src.espacios_academicos.domain.eliminar import EliminarEspacios

class EliminarEspaciosCase:
    def __init__(self,db, espaciosModel, _id):
        self.db=db
        self.espaciosModel=espaciosModel
        self._id=_id

    def run(self):
        eliminarEspacios=EliminarEspacios(self.db, self.espaciosModel, self._id)
        return eliminarEspacios.run()