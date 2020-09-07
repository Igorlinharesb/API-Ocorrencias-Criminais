from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Municipio (db.Model):
    __tablename__ = "municipio"
    id = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String)
    sigla_UF = db.Column(db.String)
    regiao = db.Column(db.String)
    mes = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    vitimas = db.Column(db.Integer)


class Estado(db.Model):
    __tablename__ = "estado"
    id = db.Column(db.Integer, primary_key=True)
    sigla_UF = db.Column(db.String)
    estado = db.Column(db.String)
    crime = db.Column(db.String)
    mes = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    vitimas = db.Column(db.Integer)
    ocorrencias = db.Column(db.Integer)
