# Módulo que define as classes de Conta (Abstrata, corrente e poupança.)

# Importa a classe base abstrata e o decorador para métodos abstratos
from abc import ABC, abstractclassmethod

# Importa a classe datetime para registrar data e hora das transações
from datetime import datetime

#
from utilitarios.exceptions import SaldoInsuficienteError


# A classe abstrata Conta serve como base para outros tipos de contas
class Conta(ABC):
    """
    Classe base abstrata para contas bancárias.
    """

    # Atributo de classe que calcula quantas contas foram criadas
    _total_contas = 0

    def __init__(self, numero: int, cliente):

        # Número da conta (atributo protegido)
        self.numero = numero

        # Saldo da conta, inicializado em 0.0 (atributo protegido)
        self._saldo = 0.0

        # Referência ao cliente dono da conta
        self.cliente = cliente

        # Lista para armazenar histórico de transações
        self._historico = []

        # Incrementa o total de contas criadas
        Conta._total_contas += 1
