import sqlite3

# Função para realizar um saque de uma conta
def sacar():
    conta = int(input("Número da conta (ID do usuário): "))
    valor = float(input("Valor a ser sacado: "))

 # Conecta ao banco de dados
    conn = sqlite3.connect('tabeladeclientes.db')
    cursor = conn.cursor()

    # Buscar a conta pelo ID do usuário
    cursor.execute("SELECT saldo FROM saldo WHERE usuario_id=?", (conta,))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[0]

        if valor <= saldo_atual:
            novo_saldo = saldo_atual - valor

            # Atualizar o saldo na tabela
            cursor.execute("UPDATE saldo SET saldo=? WHERE usuario_id=?", (novo_saldo, conta))
            conn.commit()

            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Conta não encontrada.")

    conn.close()
 # Fecha a conexão com o banco de dados