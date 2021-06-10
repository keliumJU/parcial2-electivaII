class GetSesion():
    def __init__(self, sesionesModel, id_):
        self.sesionesModel=sesionesModel
        self.id_=id_

    def run(self):
        sesion=self.sesionesModel.query.filter_by(sesion_id=self.id_).first()
        return self.sesionesModel.json(sesion)
    
    def run_native(self):
        return self.sesionesModel.query.filter_by(sesion_id=self.id_).first()