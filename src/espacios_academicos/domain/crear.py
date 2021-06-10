class CrearEspacios():
    def __init__(self,db,espaciosAcademicosModel,espaciosDTO):
        self.db=db
        self.espaciosAcademicosModel=espaciosAcademicosModel
        self.espaciosDTO=espaciosDTO
    

    def run(self):
        espacio=self.espaciosAcademicosModel(
            nombre=self.espaciosDTO.nombre,
            espacioSemestre=self.espaciosDTO.semestre
        )
        self.db.session.add(espacio)
        self.db.session.commit()
