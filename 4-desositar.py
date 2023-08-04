import sqlite3

def depositar():
    conta = int(input("Número da conta (ID do usuário): "))
    valor = float(input("Valor a ser depositado: "))

    conn = sqlite3.connect('tabeladeclientes.db')
    cursor = conn.cursor()

    # Buscar a conta pelo ID do usuário
    cursor.execute("SELECT saldo FROM saldo WHERE usuario_id=?", (conta,))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[0]
        novo_saldo = saldo_atual + valor

        # Atualizar o saldo na tabela
        cursor.execute("UPDATE saldo SET saldo=? WHERE usuario_id=?", (novo_saldo, conta))
        conn.commit()

        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")

    conn.close()