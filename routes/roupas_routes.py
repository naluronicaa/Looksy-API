from flask import Blueprint, request, jsonify
from db.database import get_db

roupas_bp = Blueprint('roupas', __name__, url_prefix='/api/roupas')

@roupas_bp.route('/', methods=['GET'])
def listar_roupas():
    db = get_db()
    roupas = db.execute('SELECT * FROM roupas').fetchall()
    return jsonify([dict(r) for r in roupas])

@roupas_bp.route('/', methods=['POST'])
def cadastrar_roupa():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO roupas (usuario_id, foto_uri, categoria, subtipo, descricao)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data.get('usuario_id'),
        data.get('foto_uri'),
        data.get('categoria'),
        data.get('subtipo'),
        data.get('descricao')
    ))
    roupa_id = cursor.lastrowid

    for uso in data.get('usos', []):
        cursor.execute('INSERT INTO usos_roupa (roupa_id, uso) VALUES (?, ?)', (roupa_id, uso))

    db.commit()
    return jsonify({'message': 'Roupa cadastrada!', 'id': roupa_id})
