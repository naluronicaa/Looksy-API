from flask import Blueprint, request, jsonify
from utils.helper import verificar_token
from models.looks_model import (
    listar_looks_usuario,
    listar_looks_recentes,
    cadastrar_look,
    deletar_look
)

looks_bp = Blueprint('looks', __name__, url_prefix='/api/looks')

@looks_bp.route('/', methods=['GET'])
@verificar_token
def get_looks():
    usuario_id = request.usuario_id
    looks = listar_looks_usuario(usuario_id)
    return jsonify(looks)

@looks_bp.route('/recentes', methods=['GET'])
@verificar_token
def get_looks_recentes():
    usuario_id = request.usuario_id
    looks = listar_looks_recentes(usuario_id)
    return jsonify(looks)

@looks_bp.route('/', methods=['POST'])
@verificar_token
def post_look():
    usuario_id = request.usuario_id
    data = request.json
    look_id = cadastrar_look(usuario_id, data)
    return jsonify({'message': 'Look cadastrado!', 'id': look_id})

@looks_bp.route('/<int:look_id>', methods=['DELETE'])
@verificar_token
def delete_look(look_id):
    usuario_id = request.usuario_id
    sucesso = deletar_look(usuario_id, look_id)

    if not sucesso:
        return jsonify({'message': 'Look não encontrado ou não pertence ao usuário'}), 404

    return jsonify({'message': 'Look deletado com sucesso!'})
