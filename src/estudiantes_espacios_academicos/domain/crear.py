class CrearLista():
    def __init__(self,db,listaDTO):
        self.db=db
        self.listaDTO=listaDTO

    def run(self):
        self.listaDTO.espaciosAcademicos.espacios.append(self.listaDTO.estudiantes)
        self.db.session.commit()