class CrearAsistencia:
    def __init__(self,db,asistenciaDTO):
        self.db=db
        self.asistenciaDTO=asistenciaDTO

    def run(self):
        self.asistenciaDTO.sesion.asistencia.append(self.asistenciaDTO.estudiante)
        self.db.session.commit()
