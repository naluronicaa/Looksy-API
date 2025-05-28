from db.database import get_db

def cadastrar_look(usuario_id, data):
    db = get_db()
    cursor = db.cursor()

    cursor.execute('''
        INSERT INTO looks (usuario_id, titulo, descricao, imagem_uri)
        VALUES (?, ?, ?, ?)
    ''', (
        usuario_id,
        data.get('titulo'),
        data.get('descricao'),
        data.get('imagem_uri'),
    ))
    look_id = cursor.lastrowid
    db.commit()
    return look_id

def listar_looks_usuario(usuario_id):
    db = get_db()
    looks = db.execute('SELECT * FROM looks WHERE usuario_id = ?', (usuario_id,)).fetchall()
    return [dict(look) for look in looks]

def listar_looks_recentes(usuario_id, limite=10):
    db = get_db()
    looks = db.execute('''
        SELECT * FROM looks
        WHERE usuario_id = ?
        ORDER BY data_criacao DESC
        LIMIT ?
    ''', (usuario_id, limite)).fetchall()
    return [dict(look) for look in looks]

def deletar_look(usuario_id, look_id):
    db = get_db()
    look = db.execute('SELECT * FROM looks WHERE id = ? AND usuario_id = ?', (look_id, usuario_id)).fetchone()

    if not look:
        return False

    db.execute('DELETE FROM looks WHERE id = ?', (look_id,))
    db.commit()
    return True
