import sqlite3


# Função para criar as tabelas de contas e saldo no banco de dados
def criar_tabelas():
    conn = sqlite3.connect('tabeladeclientes.db') 
    #Cria a tabela 'contas' caso não exista
    conn.execute('''CREATE TABLE IF NOT EXISTS contas (
                    Id INTEGER PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    rg TEXT UNIQUE,
                    senha TEXT,
                    saldo REAL DEFAULT 0.0
                    )''')
    # Cria a tabela 'saldo' caso não exista
    conn.execute('''CREATE TABLE IF NOT EXISTS saldo (
                    usuario_id INTEGER PRIMARY KEY,
                    saldo REAL DEFAULT 0.0,
                    FOREIGN KEY (usuario_id) REFERENCES contas(Id)
                    )''')
     # Fecha a conexão com o banco de dados
    conn.close()



