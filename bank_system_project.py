"""
Aplicação de Sistema Bancário em Python com POO
"""

from operacoes.banco import Banco

from utilitarios.exceptions import ContaInexistenteError, \
    SaldoInsuficienteError


# Função que exige o menu principal da aplicação
def menu_principal():

    """Menu para selecionar as opções do sistema"""

    print("\n--- Sistema Bancário Digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    return input("Escolha uma opção: ")


# Função que exibe o menu de operações de uma conta específica
def menu_conta(banco: Banco):
    """Função que exibe o menu de
    operações de uma conta específica"""

    try:

        # Solicita ao usuário o número da conta
        num_conta = int(input("Digite o número da conta: "))

        # Busca a conta no banco; pode gerar exceção se não existir
        conta = banco.buscar_conta(num_conta)

        # Loop de operações dentro da conta
        while True:

            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente} | Saldo: R${conta._saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            # Lê a opção do usuário
            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                # Deposita valor na conta
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)

            elif opcao == '2':

                # Tenta realizar um saque
                try:

                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)  # Poliformismo: depende do tipo de conta

                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")

            elif opcao == '3':

                # Exibe o extrato da conta
                conta.extrato()

            elif opcao == '4':

                # Sai do menu da conta e retorna ao menu principal
                break

            else:
                print("Opção inválida. Tente novamente.")

    # Exceção caso a conta não exista
    except ContaInexistenteError as e:
        print(f"Erro na operação: {e}")

    # Exceção para entradas inválidas (não numéricas)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")


menu_principal()
