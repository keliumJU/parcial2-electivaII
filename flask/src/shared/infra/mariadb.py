from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os

# Configure our Database
#conf={'SQLALCHEMY_DATABASE_URI':'','SQLALCHEMY_TRACK_MODIFICATIONS':''}
#conf['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:pass@dbmysql:3306/control_asistencia'
#conf['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
class ConexionDb:
    def __init__(self, app):
        self.app=app

    def new_app_with_conexion(self):
        self.app.config.from_mapping(
            # a default secret that should be overridden by instance config
            SECRET_KEY='dev',
        )
        self.app.permanent_session_lifetime=timedelta(minutes=30)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
            os.getenv('DB_USER', 'root'),
            os.getenv('DB_PASSWORD', 'pass'),
            os.getenv('DB_HOST', 'dbmysql1'),
            os.getenv('DB_NAME', 'control_asistencia')
        )
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return self.app


    def db_sql_alchemy(self, app):
        db = SQLAlchemy(app)
        return db