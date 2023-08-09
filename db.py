import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text, Column, Integer, String, DateTime, Numeric, update, inspect, insert,MetaData, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('mysql://root:admin@127.0.0.1:3306/UNBeventos')

Session = sessionmaker(bind=engine)

session = Session()
app = flask.Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'

db = SQLAlchemy(app)


class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    imagem  = db.Column(db.LargeBinary(1000000000), nullable=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time(80) ,nullable=False)
    local = db.Column(db.String(80), nullable=False)
    resumo = db.Column(db.String(1000), nullable=True)
    organizadores = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    categorias = db.Column(db.String(80), nullable=False)




class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    matricula = db.Column(db.String(80))
    curso = db.Column(db.String(80))
    email = db.Column(db.String(80))
    foto = db.Column(db.String(80))
    telefone = db.Column(db.String(80))


class incricao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    id_evento = db.Column(db.Integer)

app.app_context().push()
db.create_all()