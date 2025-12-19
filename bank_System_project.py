"""
Aplicação de Sistema Bancário em Python com POO
"""


# Função que exige o menu principal da aplicação
def menu_principal():

    """Menu para selecionar as opções do sistema"""

    print("\n--- Sistema Bancário Digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    return input("Escolha uma opção: ")
