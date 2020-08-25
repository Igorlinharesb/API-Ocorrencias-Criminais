from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Municipio (db.Model):
    __tablename__ = "municipios"



class Estado(db.Model):
    __tablename__ = "estados"