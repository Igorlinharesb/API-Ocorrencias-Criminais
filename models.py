from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Municipio (db.Model):
    __tablename__ = "municipios"
    uf = db.Column(db.String, primary_key=True)
    estado = db.Column(db.String)
    regiao = db.Column(db.String)
    mes = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    vitimas = db.Column(db.Integer)


class Estado(db.Model):
    __tablename__ = "estados"
    uf = db.Column(db.String, primary_key=True)
    estado = db.Column(db.String)
    crime = db.Column(db.String)
    mes = db.Column(db.String)
    vitimas = db.Column(db.Integer)
    ocorrencias =db.Column(db.Integer)
