from flask import Flask, jsonify
from src.shared.infra.mariadb import DB
from src.estudiantes.app.listar import ListarEstudiantesCase

app = Flask(__name__)

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    listarEstudianteCase = ListarEstudiantesCase(DB)
    return jsonify(listarEstudianteCase.run())

def create_app_api():
    app.run(debug=True, port=5100)