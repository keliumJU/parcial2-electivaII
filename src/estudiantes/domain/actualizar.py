class ActualizarEstudiantes():
    def __init__(self,db,estudiantesModel, estudiantesDTO ):
        self.db=db
        self.estudiantesModel=estudiantesModel
        self.estudiantesDTO=estudiantesDTO

    def run(self):
        estudiante=self.estudiantesModel.query.filter_by(identificacion=self.estudiantesDTO.identificacion).first()
        estudiante.nombres=self.estudiantesDTO.nombres
        estudiante.apellidos=self.estudiantesDTO.apellidos
        estudiante.celular=self.estudiantesDTO.celular
        estudiante.correo=self.estudiantesDTO.correo
        self.db.session.commit()
