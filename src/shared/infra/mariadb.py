from flask_sqlalchemy import SQLAlchemy

# Configure our Database
conf={'SQLALCHEMY_DATABASE_URI':'','SQLALCHEMY_TRACK_MODIFICATIONS':''}
conf['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/parcial2'
conf['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def db_sql_alchemy(prin):
    db = SQLAlchemy(prin)
    return db