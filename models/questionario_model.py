from db.database import get_db

def criar_questionario(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO questionario (
            usuario_id, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5,
            pergunta6, pergunta7, pergunta8, pergunta9, pergunta10
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('usuario_id'),
        data.get('pergunta1'),
        data.get('pergunta2'),
        data.get('pergunta3'),
        data.get('pergunta4'),
        data.get('pergunta5'),
        data.get('pergunta6'),
        data.get('pergunta7'),
        data.get('pergunta8'),
        data.get('pergunta9'),
        data.get('pergunta10')
    ))
    db.commit()
    return cursor.lastrowid

def obter_questionario_por_usuario(usuario_id):
    db = get_db()
    return db.execute(
        'SELECT * FROM questionario WHERE usuario_id = ?',
        (usuario_id,)
    ).fetchone()

def atualizar_questionario(usuario_id, data):
    db = get_db()
    db.execute('''
        UPDATE questionario SET
            pergunta1 = ?, pergunta2 = ?, pergunta3 = ?, pergunta4 = ?, pergunta5 = ?,
            pergunta6 = ?, pergunta7 = ?, pergunta8 = ?, pergunta9 = ?, pergunta10 = ?
        WHERE usuario_id = ?
    ''', (
        data.get('pergunta1'),
        data.get('pergunta2'),
        data.get('pergunta3'),
        data.get('pergunta4'),
        data.get('pergunta5'),
        data.get('pergunta6'),
        data.get('pergunta7'),
        data.get('pergunta8'),
        data.get('pergunta9'),
        data.get('pergunta10'),
        usuario_id
    ))
    db.commit()
