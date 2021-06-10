from src.sesiones.domain.get import GetSesion 

class GetSesionCase:
    def __init__(self,sesionModel, _id):
        self.sesionModel=sesionModel
        self._id=_id

    def run(self):
        getSesion= GetSesion(self.sesionModel, self._id)
        return getSesion.run()
    
    def run_native(self):
        getSesion= GetSesion(self.sesionModel, self._id)
        return getSesion.run_native()   