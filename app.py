from flask import Flask
from flask_cors import CORS  # 👈 importa o CORS
from routes.roupas_routes import roupas_bp
from routes.questionario_routes import questionario_bp
from routes.usuarios_routes import usuarios_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Habilita CORS para todas as rotas e origens (para testes locais)
CORS(app)

# Registra as rotas
app.register_blueprint(roupas_bp)
app.register_blueprint(questionario_bp)
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
