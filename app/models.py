from app import db
from datetime import date
from dataclasses import dataclass
from sqlalchemy.orm import Mapped


@dataclass
class Proyectos(db.Model):
    id: int
    nombre: str
    descripcion: str
    fecha_inicio: date
    fecha_termino: date
    institucion_id: int
    usuario_id: int

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    descripcion = db.Column(db.String(255))
    fecha_inicio = db.Column(db.Date)
    fecha_termino = db.Column(db.Date)
    institucion_id = db.Column(db.Integer, db.ForeignKey('instituciones.id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)


@dataclass
class Instituciones(db.Model):
    id: int
    nombre: str
    descripcion: str
    direccion: str
    fecha_de_creacion: date
    proyectos: Mapped[Proyectos]

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    descripcion = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    fecha_de_creacion = db.Column(db.Date)
    proyectos = db.relationship('Proyectos', backref='institucion', lazy=True)


@dataclass
class Usuarios(db.Model):
    id: int
    nombre: str
    apellidos: str
    rut: str
    fecha_de_nacimiento: date
    cargo: str
    edad: int
    proyectos: Mapped[Proyectos]

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellidos = db.Column(db.String(120), nullable=False)
    rut = db.Column(db.String(10), unique=True, nullable=False)
    fecha_de_nacimiento = db.Column(db.Date)
    cargo = db.Column(db.String(60), nullable=False)
    edad = db.Column(db.Integer)
    proyectos = db.relationship('Proyectos', backref='usuario_responsable', lazy=True)
