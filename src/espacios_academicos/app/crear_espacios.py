from src.espacios_academicos.domain.crear import CrearEspacios

class CrearEspaciosCase:
    def __init__(self, db, espaciosModel, espaciosDTO):
        self.db=db
        self.espaciosModel=espaciosModel
        self.espaciosDTO=espaciosDTO

    def run(self):
        crearEspacios=CrearEspacios(self.db, self.espaciosModel, self.espaciosDTO)
        return crearEspacios.run()
