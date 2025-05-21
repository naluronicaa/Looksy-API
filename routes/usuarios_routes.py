from flask import Blueprint, request, jsonify
from models.usuario_model import (
    criar_usuario,
    atualizar_usuario,
    atualizar_senha,
    deletar_usuario,
    obter_usuario_por_email
)

from utils.helper import gerar_token
from utils.helper import verificar_token

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/api/usuarios')

@usuarios_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')

    usuario = obter_usuario_por_email(email)
    if not usuario or usuario['senha'] != senha:
        return jsonify({'message': 'Credenciais inválidas'}), 401

    token = gerar_token(usuario['id'])
    return jsonify({'token': token})

# Criar usuário (extra, útil pra teste)
@usuarios_bp.route('/', methods=['POST'])
def criar():
    data = request.json
    user_id = criar_usuario(data['nome'], data['email'], data['senha'])
    return jsonify({'message': 'Usuário criado!', 'id': user_id})

# Atualizar nome e/ou email
@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
@verificar_token
def atualizar_dados(usuario_id):
    data = request.json
    sucesso = atualizar_usuario(usuario_id, data.get('nome'), data.get('email'))

    if sucesso:
        return jsonify({'message': 'Dados atualizados com sucesso!'})
    else:
        return jsonify({'message': 'Nada foi atualizado.'}), 400

# Trocar senha (recebe antiga e nova)
@usuarios_bp.route('/<int:usuario_id>/senha', methods=['PUT'])
@verificar_token
def trocar_senha(usuario_id):
    data = request.json
    senha_antiga = data.get('senha_antiga')
    nova_senha = data.get('nova_senha')

    if not senha_antiga or not nova_senha:
        return jsonify({'message': 'Informe senha antiga e nova'}), 400

    if atualizar_senha(usuario_id, senha_antiga, nova_senha):
        return jsonify({'message': 'Senha atualizada com sucesso!'})
    else:
        return jsonify({'message': 'Senha antiga incorreta ou usuário não encontrado.'}), 400

# Deletar usuário
@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
@verificar_token
def deletar(usuario_id):
    deletar_usuario(usuario_id)
    return jsonify({'message': 'Usuário deletado com sucesso!'})

# Obter dados do usuário pelo e-mail (somente se for o e-mail do próprio token)
@usuarios_bp.route('/email/<string:email>', methods=['GET'])
@verificar_token
def buscar_usuario_por_email(email):
    usuario = obter_usuario_por_email(email)

    if not usuario:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    # impede que outra pessoa consulte um email que não é o dela
    if usuario['id'] != request.usuario_id:
        return jsonify({'message': 'Acesso negado'}), 403

    return jsonify({
        'id': usuario['id'],
        'nome': usuario['nome'],
        'email': usuario['email']
    })