import jwt
import datetime
from flask import request, jsonify
from config import SECRET_KEY

def gerar_token(usuario_id):
    payload = {
        'usuario_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # expira em 24h
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verificar_token(f):
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.replace('Bearer ', '')
        if not token:
            return jsonify({'message': 'Token não fornecido'}), 401

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.usuario_id = payload['usuario_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401

        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper
