class ListarSesiones():
    def __init__(self, sesionesModel):
        self.sesionesModel=sesionesModel

    def run(self):
        return [self.sesionesModel.json(sesion) for sesion in self.sesionesModel.query.all()]