from flask import Flask, jsonify, request, Response 
from src.shared.infra.mariadb import conf, db_sql_alchemy

app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = conf['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = conf['SQLALCHEMY_DATABASE_URI'] 

db=db_sql_alchemy(app)
