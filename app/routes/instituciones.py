from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify
from app import db
from app.models import Instituciones

instituciones = Blueprint('instituciones', __name__, url_prefix='/instituciones')


@instituciones.route('/list', methods=['GET'])
def instituciones_list():
    if request.method == 'GET':
        try:
            instance = db.session.execute(db.select(Instituciones).order_by(Instituciones.id)).scalars()
            return jsonify(instance.fetchall())
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify(405)


@instituciones.route('/get/<int:institucion_id>', methods=['GET'])
def instituciones_get(institucion_id):
    if request.method == 'GET':
        try:
            instance = db.get_or_404(Instituciones, institucion_id)
            return jsonify(instance)
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify(405)        


@instituciones.route('/create', methods=['POST'])
def instituciones_create():
    if request.method == 'POST':
        try:
                instance = Instituciones(**request.json)
                db.session.add(instance)
                db.session.commit()
                return jsonify({"message": "Created"}), 200
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify(405)


@instituciones.route('/update/<int:institucion_id>', methods=['PUT', 'PATCH'])
def instituciones_update(institucion_id):
    if request.method in ['PUT', 'PATCH']:
        try:
            instance = db.session.query(Instituciones).filter_by(id=institucion_id).update(dict(**request.json))
            db.session.commit()
            return jsonify(instance)
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify(405)


@instituciones.route('/delete/<int:institucion_id>', methods=['DELETE'])
def instituciones_delete(institucion_id):
    if request.method == 'DELETE':
        try:
            instance = db.get_or_404(Instituciones, institucion_id)
            db.session.delete(instance)
            db.session.commit()
            return jsonify(instance)
        except Exception as error:
            return jsonify({"message": str(error)}), 500            
    return jsonify(405)

@instituciones.route('/list/maps', methods=['GET'])
def instituciones_list_maps():
    if request.method == 'GET':
        try:
            instance = db.session.execute(db.select(Instituciones).order_by(Instituciones.id)).scalars()
            instance = instance.fetchall()
            for institucion in instance:
                institucion.link_google_maps_direccion()
            return jsonify(instance)
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify(405)
