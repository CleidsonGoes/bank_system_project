# Módulo que define as classes de Conta (Abstrata, corrente e poupança.)

# Importa a classe base abstrata e o decorador para métodos abstratos
from abc import ABC, abstractmethod

# Importa a classe datetime para registrar data e hora das transações
from datetime import datetime

#
# from utilitarios.exceptions import SaldoInsuficienteError


# A classe abstrata Conta serve como base para outros tipos de contas
class Conta(ABC):
    """
    Classe base abstrata para contas bancárias.
    """

    # Atributo de classe que calcula quantas contas foram criadas
    _total_contas = 0

    def __init__(self, numero: int, cliente):

        # Número da conta (atributo protegido)
        self._numero = numero

        # Saldo da conta, inicializado em 0.0 (atributo protegido)
        self._saldo = 0.0

        # Referência ao cliente dono da conta
        self._cliente = cliente

        # Lista para armazenar histórico de transações
        self._historico = []

        # Incrementa o total de contas criadas
        Conta._total_contas += 1

    # Propriedade para acessar o saldo de forma controlada
    @property
    def saldo(self):

        """Getter para saldo, permitindo acesso controlado."""
        return self._saldo

    # Método de classe para consultar o número total de contas
    @classmethod
    def get_total_contas(cls):

        """Método de classe para obter o número total de contas criadas."""
        return cls._total_contas

    # Método para realizar depósitos
    def depositar(self, valor: float):

        """param valor: valor a ser depositado"""

        # Adiciona um valor ao saldo da conta.
        if valor > 0:

            # Incrementa o saldo
            self._saldo += valor

            # Registra a transação no histórico com data e hora
            self._historico.append((datetime.now), f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        else:
            print("Valor de depósito inválido.")

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def sacar(self, valor: float):

        """Método abstrato para sacar um valor. Deve ser implementado pelas subclasses."""

        pass

    # Método para exibir o extrato da conta
    def extrato(self):

        """Exibe o extrato da conta."""
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R$ {self._saldo:.2f}")
        print("Histórico de transações:")

        # Caso não haja transações registradas
        if not self._historico:
            print("Nenhuma transação registrada.")

        # Percorre o histórico e exibe cada transação
        for data, transacao in self._historico:
            print(f"- {data.strtime('%d/%m/%Y %H:%M:%S')}: {transacao}")

        print("---------------------------\n")


# ================= TESTE =================
if __name__ == "__main__":

    poupanca = Conta(78, "J")
    # print(poupanca.)
