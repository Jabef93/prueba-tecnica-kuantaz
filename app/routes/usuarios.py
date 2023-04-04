from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify
from app import db
from app.models import Usuarios

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@usuarios.route('/list', methods=['GET'])
def usuarios_list():
    if request.method == 'GET':
        try:
            instance = db.session.execute(db.select(Usuarios).order_by(Usuarios.id)).scalars()
            return jsonify(instance.fetchall())
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify({"message": "Method Not Allowed"}), 405


@usuarios.route('/get/<string:usuario_rut>', methods=['GET'])
def usuarios_get(usuario_rut):
    if request.method == 'GET':
        try:
            instance = db.session.query(Usuarios).filter_by(rut=usuario_rut).first_or_404()
            return jsonify(instance)
        except Exception as error:
            return jsonify({"message": str(error)}), 500
    return jsonify({"message": "Method Not Allowed"}), 405
