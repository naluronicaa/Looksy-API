from db.database import get_db

def criar_usuario(nome, email, senha):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    db.commit()
    return cursor.lastrowid

def obter_usuario_por_id(usuario_id):
    db = get_db()
    return db.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,)).fetchone()

def obter_usuario_por_email(email):
    db = get_db()
    return db.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()

def atualizar_usuario(usuario_id, nome=None, email=None):
    db = get_db()
    campos = []
    valores = []

    if nome:
        campos.append('nome = ?')
        valores.append(nome)
    if email:
        campos.append('email = ?')
        valores.append(email)

    if not campos:
        return 0

    valores.append(usuario_id)
    query = f'UPDATE usuarios SET {", ".join(campos)} WHERE id = ?'
    db.execute(query, tuple(valores))
    db.commit()
    return 1

def atualizar_senha(usuario_id, senha_antiga, nova_senha):
    db = get_db()
    usuario = obter_usuario_por_id(usuario_id)

    if not usuario or usuario['senha'] != senha_antiga:
        return False

    db.execute('UPDATE usuarios SET senha = ? WHERE id = ?', (nova_senha, usuario_id))
    db.commit()
    return True

def deletar_usuario(usuario_id):
    db = get_db()
    db.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
    db.commit()
