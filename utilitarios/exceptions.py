# Módulos para exceções customizadas da aplicação.

# Define a exceção para saldo insuficiente em operações de saque
class SaldoInsuficienteError(Exception):
    """
    Exceção levantada quando uma operação de saque excede o saldo disponível.
    """
    def __init__(self, saldo_atual, valor_saque,
                 mensagem="Saldo insuficiente para realizar o saque"):

        # Saldo atual da conta no momento do erro
        self.saldo_atual = saldo_atual

        # Valor solicitado para saque
        self.valor_saque = valor_saque

        # Mensagem detalhada de erro com saldo atual e valor do saque
        self.mensagem = f"{mensagem} Saldo atual: R$ {saldo_atual:.2f}, tentativa de saque: R$ {valor_saque:.2f}."
