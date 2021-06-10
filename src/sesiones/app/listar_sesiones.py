from src.sesiones.domain.listar import ListarSesiones 

class ListarSesionesCase:
    def __init__(self,sesionesModel):
        self.sesionesModel=sesionesModel

    def run(self):
        listarSesiones= ListarSesiones(self.sesionesModel)
        return listarSesiones.run()