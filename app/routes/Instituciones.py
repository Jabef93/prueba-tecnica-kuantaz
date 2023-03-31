from flask import Blueprint, jsonify
from app.models.Instituciones import InstitucionesModel

main = Blueprint('instituciones', __name__)


@main.route('/')
def list_instituciones():
    try:
        instituciones = InstitucionesModel.get_instituciones()
        return jsonify(instituciones)
    except Exception as error:
        return jsonify({"message": str(error)}), 500

