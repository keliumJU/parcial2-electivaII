

from flask import Flask, render_template, request, Response, jsonify
#from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy
#import os
from src.shared.infra.mariadb import ConexionDb 
app = Flask(__name__)
conexion = ConexionDb(app)
app=conexion.new_app_with_conexion()
db=conexion.db_sql_alchemy(app)

'''
app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
)
app.permanent_session_lifetime=timedelta(minutes=30)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'root'),
    os.getenv('DB_PASSWORD', 'pass'),
    os.getenv('DB_HOST', 'dbmysql1'),
    os.getenv('DB_NAME', 'control_asistencia')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
'''
#from src.shared.infra.base_api import * 
from src.shared.infra.Modelos import *
#from apps.api.Modelos import *
from src.shared.infra.dto import estudiantes_dto, espacios_dto, lista_clase_dto, sesiones_dto, asistencia_dto, faltantes_dto 
from src.estudiantes.app import listar, crear, actualizar, eliminar, get_estudiante
from src.semestres.app import listar_semestre, get_semestre
from src.espacios_academicos.app import listar_espacios, crear_espacios, actualizar_espacios, eliminar_espacios, get_espacio
from src.estudiantes_espacios_academicos.app import crear_lista, eliminar_estudiante_lista
from src.sesiones.app import listar_sesiones, crear_sesiones, get_sesion
from src.asistencia.app import crear_asistencia, listar_faltantes


#Estudiantes

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    listarEstudianteCase = listar.ListarEstudiantesCase(Estudiantes)
    return jsonify(listarEstudianteCase.run())

@app.route('/estudiantes/id',methods=['POST'])
def get_estudiante_by_id():
    if request.method=='POST':
        id_estudiante=request.form["identificacion"]
        getEstudianteCase= get_estudiante.GetEstudianteCase(Estudiantes, id_estudiante)
        return jsonify(getEstudianteCase.run()) 

@app.route('/estudiantes', methods=['POST'])
def crear_estudiantes():
    if request.method=='POST':
        identificacion=request.form["identificacion"]
        nombres=request.form["nombres"]
        apellidos=request.form["apellidos"]
        celular=request.form["celular"]
        correo=request.form["correo"]

        estudianteDto=estudiantes_dto.EstudiantesDTO(
            identificacion=identificacion,
            nombres=nombres,
            apellidos=apellidos,
            celular=celular,
            correo=correo
        )
        crearEstudiantes=crear.CrearEstudiantesCase(db,Estudiantes,estudianteDto)
        crearEstudiantes.run()
        response = Response("Estudiante Agregado", 201, mimetype='application/json')
        return response       

@app.route('/estudiantes',methods=['PUT'])
def guardar_estudiante():
    if request.method=='PUT':
        identificacion=request.form["identificacion"]
        nombres=request.form["nombres"]
        apellidos=request.form["apellidos"]
        celular=request.form["celular"]
        correo=request.form["correo"]

        estudianteDto=estudiantes_dto.EstudiantesDTO(
            identificacion=identificacion,
            nombres=nombres,
            apellidos=apellidos,
            celular=celular,
            correo=correo
        )
        actualizarEstudiante=actualizar.ActualizarEstudiantesCase(db,Estudiantes,estudianteDto)
        actualizarEstudiante.run()
        response = Response("Estudiante Actualizado", 201, mimetype='application/json')
        return response       
@app.route('/estudiantes',methods=['DELETE'])
def borrar_estudiante():
    if request.method=='DELETE':
        identificacion=request.form["identificacion"]
        eliminarEstudiante=eliminar.EliminarEstudiantesCase(db,Estudiantes,identificacion)
        eliminarEstudiante.run()
        response = Response("Estudiante Eliminado", 201, mimetype='application/json')
        return response  

#Semestres

@app.route('/semestres',methods=['GET'])
def listar_semestres():
    listarSemestresCase = listar_semestre.ListarSemestresCase(Semestres)
    return jsonify(listarSemestresCase.run())    

@app.route('/semestres',methods=['POST'])
def get_semestre_by_id():
    if request.method=='POST':
        id_semestre=request.form["semestre"]
        getSemestreCase = get_semestre.GetSemestreCase(id_semestre, Semestres)
        return jsonify(getSemestreCase.run())    


#Espacios Academicos

@app.route('/espacios_academicos', methods=['GET'])
def listar_espacios_academicos():
    listarEspaciosAcademicos = listar_espacios.ListarEspaciosCase(EspaciosAcademicos)
    return jsonify(listarEspaciosAcademicos.run())

@app.route('/espacios_academicos/id',methods=['POST'])
def get_espacio_by_id():
    if request.method=='POST':
        espacio_id=request.form["espacio_id"]
        getEspacioCase= get_espacio.GetEspacioCase(EspaciosAcademicos,espacio_id)
        return jsonify(getEspacioCase.run()) 

@app.route('/espacios_academicos',methods=['POST'])
def crear_espacio():
    if request.method=='POST':
        nombre=request.form["nombre"]
        id_semestre=request.form["semestre"]
        
        #semestre=semestresController.get(id_semestre)
        semestre=get_semestre.GetSemestreCase(id_semestre, Semestres)

        espacioDto=espacios_dto.EspaciosDTO(
            nombre=nombre,
            semestre=semestre.run_native()
        )

        crearEspacio=crear_espacios.CrearEspaciosCase(db,EspaciosAcademicos,espacioDto)
        crearEspacio.run()
        response = Response("Espacio Agregado", 201, mimetype='application/json')
        return response       

@app.route('/espacios_academicos', methods=['PUT'])
def editar_espacio():
    if request.method=='PUT':
        espacio_id=request.form["id"]
        nombre=request.form["nombre"]
        id_semestre=request.form["semestre"]
       
        semestre=get_semestre.GetSemestreCase(id_semestre, Semestres)

        espacioDto=espacios_dto.EspaciosDTO(
            nombre=nombre,
            semestre=semestre.run_native()
        )

        actualizarEspacio=actualizar_espacios.ActualizarEspacioCase(db,EspaciosAcademicos,espacioDto, espacio_id)
        actualizarEspacio.run()
        response = Response("Espacio Actualizado", 201, mimetype='application/json')
        return response       

@app.route('/espacios_academicos',methods=['DELETE'])
def borrar_espacio():
    if request.method=='DELETE':
        espacio_id=request.form["id"]

        eliminarEspacio=eliminar_espacios.EliminarEspaciosCase(db,EspaciosAcademicos,espacio_id)
        eliminarEspacio.run()
        response = Response("Espacios Academico Eliminado", 201, mimetype='application/json')
        return response


#Estudiantes espacios academicos

@app.route('/lista_clase',methods=['POST'])
def agregar_estudiante_espacio():
    if request.method=='POST':
        id_espacio=request.form["id_espacio"]
        id_estudiante=request.form["id_estudiante"]

        estudiante=get_estudiante.GetEstudianteCase(Estudiantes, id_estudiante)
        espacio=get_espacio.GetEspacioCase(EspaciosAcademicos,id_espacio)

        listaClaseDto=lista_clase_dto.ListaClaseDTO(
            espaciosAcademicos=espacio.run_native(),
            estudiantes=estudiante.run_native()
        ) 

        crearListaClase=crear_lista.CrearListaCase(db,listaClaseDto)
        crearListaClase.run()
        response = Response("Espacio Agregado", 201, mimetype='application/json')
        return response  

@app.route('/lista_clase',methods=['DELETE'])
def borrar_estudiante_espacio():
    if request.method=='DELETE':
        id_estudiante=request.form["id"]
        id_espacio=request.form["id_espacio"]

        estudiante=get_estudiante.GetEstudianteCase(Estudiantes, id_estudiante)
        espacio=get_espacio.GetEspacioCase(EspaciosAcademicos,id_espacio)

        listaClaseDto=lista_clase_dto.ListaClaseDTO(
            espaciosAcademicos=espacio.run_native(),
            estudiantes=estudiante.run_native()
        ) 

        eliminarEstLista=eliminar_estudiante_lista.EliminarEstudianteListaCase(db,listaClaseDto)
        eliminarEstLista.run()
        response = Response("Estudiante Elmiminado del Espacio Academico", 201, mimetype='application/json')
        return response  

# Sesiones

@app.route('/sesiones', methods=['GET'])
def listar_sesiones_fun():
    listarSesiones= listar_sesiones.ListarSesionesCase(Sesiones)
    return jsonify(listarSesiones.run())

@app.route('/sesiones',methods=['POST'])
def crear_sesion():
    if request.method=='POST':
        fecha=request.form["fecha"]
        hora_ini=request.form["hora_ini"]
        hora_end=request.form["hora_end"]
        id_espacio=request.form["id_espacio"]

        espacio=get_espacio.GetEspacioCase(EspaciosAcademicos,id_espacio)

        sesionDto=sesiones_dto.SesionesDTO(
            fecha=fecha,
            hora_ini=hora_ini,
            hora_end=hora_end,
            espacios=espacio.run_native()
        )
        crearSesion=crear_sesiones.CrearSesionesCase(db,Sesiones, sesionDto)
        crearSesion.run()
        response = Response("Sesion creada satisfactoriamente", 201, mimetype='application/json')
        return response 

@app.route('/sesiones/id',methods=['POST'])
def get_sesion_by_id():
    if request.method=='POST':
        id_sesion=request.form["id_sesion"]
        getSesionCase= get_sesion.GetSesionCase(Sesiones,id_sesion)
        return jsonify(getSesionCase.run()) 

# Asistencia

@app.route('/asistencia',methods=['POST'])
def registro_asistencia():
    if request.method=='POST':
        id_estudiante=request.form["id_estudiante"]
        id_sesion=request.form["id_sesion"]

        getEstudianteCase= get_estudiante.GetEstudianteCase(Estudiantes, id_estudiante)
        getSesionCase= get_sesion.GetSesionCase(Sesiones,id_sesion)

        asistenciaDto=asistencia_dto.AsistenciaDTO(
            estudiante=getEstudianteCase.run_native(),
            sesion=getSesionCase.run_native()
        )
        crearAsistencia=crear_asistencia.CrearAsistenciaCase(db,asistenciaDto)
        crearAsistencia.run()
        response = Response("Estudiante registrado exitosamente en la asistencia", 201, mimetype='application/json')
        return response 

@app.route('/asistencia/faltantes',methods=['POST'])
def listar_estudiantes_faltantes():
    if request.method=='POST':
        id_espacio=request.form["id_espacio"]
        id_sesion=request.form["id_sesion"]

        getSesionCase= get_sesion.GetSesionCase(Sesiones,id_sesion)
        getEspacioCase= get_espacio.GetEspacioCase(EspaciosAcademicos,id_espacio)
        
        faltantesDto=faltantes_dto.FaltantesDTO(
            sesion=getSesionCase.run_native(),
            espacio=getEspacioCase.run_native()
        )

        listarFaltantesCase=listar_faltantes.ListarFaltantesCase(faltantesDto,get_estudiante,Estudiantes)
        return jsonify(listarFaltantesCase.run())


def create_app():
    app.run(debug=True, port=5000)
    return app