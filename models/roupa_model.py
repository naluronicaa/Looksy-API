from db.database import get_db

def listar_roupas_usuario(usuario_id):
    db = get_db()
    roupas = db.execute('SELECT * FROM roupas WHERE usuario_id = ?', (usuario_id,)).fetchall()

    resultado = []
    for roupa in roupas:
        usos = db.execute('SELECT uso FROM usos_roupa WHERE roupa_id = ?', (roupa['id'],)).fetchall()
        resultado.append({
            **dict(roupa),
            'usos': [u['uso'] for u in usos]
        })
    return resultado

def listar_roupas_recentes(usuario_id, limite=10):
    db = get_db()
    roupas = db.execute('''
        SELECT * FROM roupas
        WHERE usuario_id = ?
        ORDER BY data_criacao DESC
        LIMIT ?
    ''', (usuario_id, limite)).fetchall()

    resultado = []
    for roupa in roupas:
        usos = db.execute('SELECT uso FROM usos_roupa WHERE roupa_id = ?', (roupa['id'],)).fetchall()
        resultado.append({
            **dict(roupa),
            'usos': [u['uso'] for u in usos]
        })
    return resultado

def cadastrar_roupa(usuario_id, data):
    db = get_db()
    cursor = db.cursor()

    cursor.execute('''
        INSERT INTO roupas (usuario_id, foto_uri, categoria, subtipo, descricao)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        usuario_id,
        data.get('foto_uri'),
        data.get('categoria'),
        data.get('subtipo'),
        data.get('descricao')
    ))
    roupa_id = cursor.lastrowid

    for uso in data.get('usos', []):
        cursor.execute('INSERT INTO usos_roupa (roupa_id, uso) VALUES (?, ?)', (roupa_id, uso))

    db.commit()
    return roupa_id

def deletar_roupa(usuario_id, roupa_id):
    db = get_db()
    roupa = db.execute('SELECT * FROM roupas WHERE id = ? AND usuario_id = ?', (roupa_id, usuario_id)).fetchone()

    if not roupa:
        return False

    db.execute('DELETE FROM usos_roupa WHERE roupa_id = ?', (roupa_id,))
    db.execute('DELETE FROM roupas WHERE id = ?', (roupa_id,))
    db.commit()
    return True
