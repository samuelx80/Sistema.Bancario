import sqlite3

# Função para verificar o saldo de uma conta
def verificar_saldo():
    conta = int(input("Número da conta (ID do usuário): "))

    # Conecta ao banco de dados
    conn = sqlite3.connect('tabeladeclientes.db')
    cursor = conn.cursor()

    # Buscar a conta pelo ID do usuário
    cursor.execute("SELECT saldo FROM saldo WHERE usuario_id=?", (conta,))
    resultado = cursor.fetchone()

    if resultado:
        saldo = resultado[0]
        print(f"Saldo disponível: R$ {saldo:.2f}")
    else:
        print("Conta não encontrada.")
 # Fecha a conexão com o banco de dados
    conn.close()



