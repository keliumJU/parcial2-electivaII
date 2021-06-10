from src.asistencia.domain.crear import CrearAsistencia 

class CrearAsistenciaCase:
    def __init__(self,db,asistenciaDTO):
        self.db=db
        self.asistenciaDTO=asistenciaDTO

    def run(self):
        crearAsistencia=CrearAsistencia(self.db,self.asistenciaDTO)
        return crearAsistencia.run()
