class CrearEstudiantes():
    def __init__(self,db,estudiantesModel,estudiantesDTO):
        self.db=db
        self.estudiantesModel=estudiantesModel
        self.estudiantesDTO=estudiantesDTO
    
    def run(self):
        estudiante=self.estudiantesModel(identificacion=self.estudiantesDTO.identificacion,
                        nombres=self.estudiantesDTO.nombres,
                        apellidos=self.estudiantesDTO.apellidos,
                        celular=self.estudiantesDTO.celular,
                        correo=self.estudiantesDTO.correo,
                        )
        self.db.session.add(estudiante)
        self.db.session.commit()
        



