from src.sesiones.domain.crear import CrearSesiones 

class CrearSesionesCase:
    def __init__(self,db,sesionesModel,sesionesDTO):
        self.db=db
        self.sesionesModel=sesionesModel
        self.sesionesDTO=sesionesDTO

    def run(self):
        crearSesiones=CrearSesiones(self.db, self.sesionesModel, self.sesionesDTO)
        return crearSesiones.run()
