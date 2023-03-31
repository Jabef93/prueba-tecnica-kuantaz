from app import db
from datetime import date


class Instituciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    descripcion = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    fecha_de_creacion = db.Column(db.Date)


class Proyectos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    descripcion = db.Column(db.String(255))
    fecha_inicio = db.Column(db.Date)
    fecha_termino = db.Column(db.Date)


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellidos = db.Column(db.String(120), nullable=False)
    rut = db.Column(db.String(10), unique=True, nullable=False)
    fecha_de_nacimiento = db.Column(db.Date)
    cargo = db.Column(db.String(60), nullable=False)
    edad = db.Column(db.Integer)

    """ id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) """
