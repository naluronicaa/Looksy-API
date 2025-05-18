from flask import Blueprint, request, jsonify
from utils.helper import verificar_token
from models.questionario_model import (
    criar_questionario,
    obter_questionario_por_usuario,
    atualizar_questionario
)

questionario_bp = Blueprint('questionario', __name__, url_prefix='/api/questionario')

# Criar novo questionário
@questionario_bp.route('/', methods=['POST'])
@verificar_token
def salvar_respostas():
    data = request.json
    data['usuario_id'] = request.usuario_id  # garante que seja o usuário logado
    questionario_id = criar_questionario(data)
    return jsonify({'message': 'Questionário salvo com sucesso!', 'id': questionario_id})

# Buscar questionário do usuário logado
@questionario_bp.route('/<int:usuario_id>', methods=['GET'])
@verificar_token
def obter_respostas(usuario_id):
    if usuario_id != request.usuario_id:
        return jsonify({'message': 'Acesso negado'}), 403

    resposta = obter_questionario_por_usuario(usuario_id)
    if resposta:
        return jsonify(dict(resposta))
    else:
        return jsonify({'message': 'Questionário não encontrado'}), 404

# Atualizar questionário do usuário logado
@questionario_bp.route('/<int:usuario_id>', methods=['PUT'])
@verificar_token
def atualizar_respostas(usuario_id):
    if usuario_id != request.usuario_id:
        return jsonify({'message': 'Acesso negado'}), 403

    existente = obter_questionario_por_usuario(usuario_id)
    if not existente:
        return jsonify({'message': 'Questionário não encontrado'}), 404

    data = request.json
    atualizar_questionario(usuario_id, data)
    return jsonify({'message': 'Questionário atualizado com sucesso!'})
