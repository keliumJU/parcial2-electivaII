class EliminarEstudiantes():
    def __init__(self,db,estudiantesModel,_id):
        self.db=db
        self.estudiantesModel=estudiantesModel
        self._id=_id
    
    def run(self):
        self.estudiantesModel.query.filter_by(identificacion=self._id).delete()
        self.db.session.commit()