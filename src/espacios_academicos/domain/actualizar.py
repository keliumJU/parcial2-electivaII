class ActualizarEspacio():
    def __init__(self,db,espacioModel, espaciosDTO, _id):
        self.db=db
        self.espacioModel=espacioModel
        self.espaciosDTO=espaciosDTO
        self._id=_id

    def run(self):
        espacio=self.espacioModel.query.filter_by(espacio_id=self._id).first()
        espacio.nombre=self.espaciosDTO.nombre
        espacio.espacioSemestre=self.espaciosDTO.semestre
        self.db.session.commit()
