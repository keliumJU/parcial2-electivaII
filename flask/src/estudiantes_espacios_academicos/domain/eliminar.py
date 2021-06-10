class EliminarEstudianteLista():
    def __init__(self,db,listaDTO):
        self.db=db
        self.listaDTO=listaDTO
    
    def run(self):
        self.listaDTO.espaciosAcademicos.espacios.remove(self.listaDTO.estudiantes)
        self.db.session.commit()