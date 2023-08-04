import sqlite3

# Função principal do programa
def main():
    criar_tabelas()
 # Cria as tabelas se não existirem
    while True:
        print("\n--- Menu ---")
        print("1. Criar conta")
        print("2. Verificar saldo")
        print("3. Depositar dinheiro")
        print("4. Sacar dinheiro")
        print("5. Encerrar o atendimento")

        option = input("Escolha a opção desejada: ")

        if option == '1':
            criar_conta()
        elif option == '2':
            verificar_saldo()
        elif option == '3':
            depositar()
        elif option == '4':
            sacar()
        elif option == '5':
            print("Atendimento encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
