from database.db import get_connection
from .entities.Instituciones import Instituciones


class InstitucionesModel():
    @classmethod
    def get_instituciones(self):
        try:
            connection = get_connection()
            instituciones = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, descripcion, direccion, fecha_de_creacion FROM public.instituciones")
                result_set = cursor.fetchall()
                #import ipdb; ipdb.set_trace()
                for row in result_set:
                    institucion = Instituciones(id=row[0], nombre=row[1], descripcion=row[2], direccion=row[3], fecha_de_creacion=row[4])
                    instituciones.append(institucion.to_json())
            connection.close()
            return instituciones
        except Exception as error:
            raise Exception(error)
