import sqlite3

def criar_conta():
    nome = input("Nome completo: ")
    email = input("Email: ")
    rg = input("RG: ")
    senha = input("Digite a senha: ")

    conn = sqlite3.connect('tabeladeclientes.db')
    cursor = conn.cursor()

    # Verifica se o RG já está cadastrado
    cursor.execute("SELECT COUNT(*) FROM contas WHERE rg=?", (rg,))
    if cursor.fetchone()[0] > 0:
        print("Já existe uma conta com esse RG.")
        return

    # Inserir o novo registro na tabela 'contas'
    cursor.execute("INSERT INTO contas (nome, email, rg, senha) VALUES (?, ?, ?, ?)", (nome, email, rg, senha))
    conn.commit()

    # Recuperar o ID do usuário recém-criado
    cursor.execute("SELECT last_insert_rowid()")
    usuario_id = cursor.fetchone()[0]   
    print(f"{nome} ({email}) - ID do cliente:", usuario_id)


    # Inserir o novo registro na tabela 'saldo'
    cursor.execute("INSERT INTO saldo (usuario_id, saldo) VALUES (?, ?)", (usuario_id, 0.0))
    conn.commit()

    print("Conta criada com sucesso!")

    conn.close()