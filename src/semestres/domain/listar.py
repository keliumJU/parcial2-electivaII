class ListarEstudiantes():
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        cursor = self.DB.cursor(dictionary=True)

        cursor.execute('select * from estudiante')

        estudiantes = cursor.fetchall()
        
        cursor.close()
        
        return estudiantes