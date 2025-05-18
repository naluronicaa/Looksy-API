from flask import Blueprint, request, jsonify
from utils.helper import verificar_token
from models.roupa_model import (
    listar_roupas_usuario,
    listar_roupas_recentes,
    cadastrar_roupa,
    deletar_roupa
)

roupas_bp = Blueprint('roupas', __name__, url_prefix='/api/roupas')

@roupas_bp.route('/', methods=['GET'])
@verificar_token
def get_roupas():
    usuario_id = request.usuario_id
    roupas = listar_roupas_usuario(usuario_id)
    return jsonify(roupas)

@roupas_bp.route('/recentes', methods=['GET'])
@verificar_token
def get_roupas_recentes():
    usuario_id = request.usuario_id
    roupas = listar_roupas_recentes(usuario_id)
    return jsonify(roupas)

@roupas_bp.route('/', methods=['POST'])
@verificar_token
def post_roupa():
    usuario_id = request.usuario_id
    data = request.json
    roupa_id = cadastrar_roupa(usuario_id, data)
    return jsonify({'message': 'Roupa cadastrada!', 'id': roupa_id})

@roupas_bp.route('/<int:roupa_id>', methods=['DELETE'])
@verificar_token
def delete_roupa(roupa_id):
    usuario_id = request.usuario_id
    sucesso = deletar_roupa(usuario_id, roupa_id)

    if not sucesso:
        return jsonify({'message': 'Roupa não encontrada ou não pertence ao usuário'}), 404

    return jsonify({'message': 'Roupa deletada com sucesso!'})
