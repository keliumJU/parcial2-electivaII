class EliminarEspacios():
    def __init__(self,db,espaciosModel,_id):
        self.db=db
        self.espaciosModel=espaciosModel
        self._id=_id
    
    def run(self):
        self.espaciosModel.query.filter_by(espacio_id=self._id).delete()
        self.db.session.commit()