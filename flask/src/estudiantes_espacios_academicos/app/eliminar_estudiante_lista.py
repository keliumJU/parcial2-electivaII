from src.estudiantes_espacios_academicos.domain.eliminar import EliminarEstudianteLista 

class EliminarEstudianteListaCase:
    def __init__(self,db, listaDTO):
        self.db=db
        self.listaDTO=listaDTO

    def run(self):
        eliminarEstudianteLista=EliminarEstudianteLista(self.db, self.listaDTO)
        return eliminarEstudianteLista.run()