from src.estudiantes_espacios_academicos.domain.crear import CrearLista 

class CrearListaCase:
    def __init__(self,db,listaDTO):
        self.db=db
        self.listaDTO=listaDTO

    def run(self):
        crearLista=CrearLista(self.db,self.listaDTO)
        return crearLista.run()
