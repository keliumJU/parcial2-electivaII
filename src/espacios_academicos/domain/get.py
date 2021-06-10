class GetEspacio():
    def __init__(self, espacioModel, id_):
        self.espacioModel=espacioModel
        self.id_=id_

    def run(self):
        espacio=self.espacioModel.query.filter_by(espacio_id=self.id_).first()
        return self.espacioModel.json(espacio)
    
    def run_native(self):
        return self.espacioModel.query.filter_by(espacio_id=self.id_).first()