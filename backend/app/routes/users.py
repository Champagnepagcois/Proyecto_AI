from flask import Blueprint, jsonify

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['GET'])
def get_all_users():
    return jsonify({"users": "Lista de usuarios"})

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({"user": f"Detalles del usuario {user_id}"})