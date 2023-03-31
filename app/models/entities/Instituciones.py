class Instituciones():

    def __init__(self, id, nombre=None, descripcion=None, direccion=None, fecha_de_creacion=None) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.direccion = direccion
        self.fecha_de_creacion = fecha_de_creacion

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'direccion': self.direccion,
            'fecha_de_creacion': self.fecha_de_creacion
        }
