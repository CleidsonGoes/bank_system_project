"""
Módulo que define a classe principal do Banco,
que gerencia clientes e contas.
"""

# Importa a classe Cliente
from entidades.cliente import Cliente

# Importa a classe base Conta e suas subclasses (Corrente e Poupança)
# from entidades.conta import Conta, ContaCorrente, ContaPoupanca


# Define a classe Banco
class Banco:
    """
    Classe que gerencia as operações do banco.
    Demonstra Composição, pois "tem" clientes e contas.
    """

    def __init__(self, nome: str):

        # Nome do banco
        self.nome = nome

        # Dicionário de clientes (chave: CPF, valor: objeto Cliente)
        self._clientes = {}

        # Dicionário de contas (chave: número da conta, valor: objeto Conta)
        self._contas = {}

    # Método para adicionar um novo cliente ao banco
    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:

        """Cria e adiciona um novo cliente ao banco."""
        if cpf in self._clientes:
            print("Erro: Cliente com este CPF já cadastrado.")
            return self._clientes[cpf]

        # Cria objeto Cliente e adiciona ao dicionário
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} adicionado com sucesso!")


# if __name__ == "__main__":
