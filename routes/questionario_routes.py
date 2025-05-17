from flask import Blueprint, request, jsonify
from db.database import get_db

questionario_bp = Blueprint('questionario', __name__, url_prefix='/api/questionario')

@questionario_bp.route('/', methods=['POST'])
def salvar_respostas():
    data = request.json
    db = get_db()
    db.execute('''
        INSERT INTO questionario (
            usuario_id, estilo, ocasioes, clima, conforto_ou_elegancia,
            cores, valoriza, disfarca, nao_usaria, ama_usar, referencias
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('usuario_id'), data.get('estilo'), data.get('ocasioes'),
        data.get('clima'), data.get('conforto_ou_elegancia'), data.get('cores'),
        data.get('valoriza'), data.get('disfarca'), data.get('nao_usaria'),
        data.get('ama_usar'), data.get('referencias')
    ))
    db.commit()
    return jsonify({'message': 'Questionário salvo com sucesso!'})
