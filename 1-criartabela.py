import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('tabeladeclientes.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS contas (
                    Id INTEGER PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    rg TEXT UNIQUE,
                    senha TEXT,
                    saldo REAL DEFAULT 0.0
                    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS saldo (
                    usuario_id INTEGER PRIMARY KEY,
                    saldo REAL DEFAULT 0.0,
                    FOREIGN KEY (usuario_id) REFERENCES contas(Id)
                    )''')

    conn.close()



