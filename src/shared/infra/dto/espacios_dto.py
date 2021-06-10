from src.shared.infra.Modelos import Semestres

class EspaciosDTO():
    nombre:str
    semestre:Semestres

    def __init__(self,nombre,semestre):
        self.nombre=nombre
        self.semestre=semestre
