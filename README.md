# 👗 Looksy API

API RESTful do projeto **Looksy**, onde usuários podem cadastrar roupas, responder a um questionário de estilo e gerenciar seus dados com segurança usando Flask e autenticação JWT.

---

## 🔐 Autenticação com JWT

A maioria dos endpoints requer autenticação. Após o login, o servidor retorna um **token JWT** que deve ser incluído nas requisições:

Authorization: Bearer SEU_TOKEN_AQUI


---

## 📌 Endpoints da API

### 🔑 Autenticação
| Método | Rota                      | Descrição               | Requer Token |
|--------|---------------------------|--------------------------|--------------|
| POST   | `/api/usuarios/`          | Criar novo usuário       | ❌           |
| POST   | `/api/usuarios/login`     | Login e geração de token | ❌           |

---

### 👤 Usuário
| Método | Rota                            | Descrição                          | Requer Token |
|--------|----------------------------------|-------------------------------------|--------------|
| PUT    | `/api/usuarios/<id>`            | Atualizar nome e/ou e-mail          | ✅           |
| PUT    | `/api/usuarios/<id>/senha`      | Trocar senha (com verificação)      | ✅           |
| DELETE | `/api/usuarios/<id>`            | Deletar conta                       | ✅           |

---

### 👗 Roupas
| Método | Rota                          | Descrição                                | Requer Token |
|--------|-------------------------------|-------------------------------------------|--------------|
| GET    | `/api/roupas/`                | Listar roupas do usuário                  | ✅           |
| GET    | `/api/roupas/recentes`        | Listar as 10 roupas mais recentes         | ✅           |
| POST   | `/api/roupas/`                | Cadastrar nova roupa                      | ✅           |
| DELETE | `/api/roupas/<id>`            | Excluir roupa (se for do usuário)         | ✅           |

---

### 📝 Questionário
| Método | Rota                               | Descrição                             | Requer Token |
|--------|------------------------------------|----------------------------------------|--------------|
| POST   | `/api/questionario/`              | Salvar respostas                       | ✅           |
| GET    | `/api/questionario/<usuario_id>`  | Buscar respostas                       | ✅           |
| PUT    | `/api/questionario/<usuario_id>`  | Atualizar respostas                    | ✅           |

---

## ⚙️ Configuração

Todas as configurações estão centralizadas no arquivo `config.py`.  
Exemplo:

<pre>
  # config.py 
  SECRET_KEY = 'sua_chave_secreta_aqui'
  DATABASE = 'database.db
</pre>

Para o secret_key:
[Gerador de JwtSecret](https://jwtsecret.com/generate)

---

### 🧱 Geração do banco de dados
O projeto inclui um notebook Python (.ipynb) que cria automaticamente todas as tabelas necessárias no arquivo SQLite (looksy.db), incluindo:

Tabela de usuários

Tabela de roupas

Tabela de usos das roupas

Tabela de respostas do questionário

Basta rodar o notebook antes de iniciar o servidor.

---

### 🧪 Testes com Postman, Insomnia ou ThunderClient
Inclua o token JWT no header:

makefile
Copiar
Editar
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
