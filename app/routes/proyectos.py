from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify
from app import db
from app.models import Proyectos

proyectos = Blueprint('proyectos', __name__, url_prefix='/proyectos')


@proyectos.route('/list', methods=['GET'])
def proyectos_list():
    if request.method == 'GET':
        try:
            instance = db.session.execute(db.select(Proyectos).order_by(Proyectos.id)).scalars()
            return jsonify(instance.fetchall())
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify(405)
