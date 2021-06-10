class CrearSesiones():
    def __init__(self,db,sesionesModel,sesionesDTO):
        self.db=db
        self.sesionesModel=sesionesModel
        self.sesionesDTO=sesionesDTO
    
    def run(self):
        sesion=self.sesionesModel(
            fecha=self.sesionesDTO.fecha,
            hora_ini=self.sesionesDTO.hora_ini,
            hora_fin=self.sesionesDTO.hora_end,
            espacioSesion=self.sesionesDTO.espacios
        )
        self.db.session.add(sesion)
        self.db.session.commit()
        



