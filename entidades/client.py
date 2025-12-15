# Aplicação Full-Stack de Sistema Bancário em Python com Programação Orientada a Objetos

# Módulo da Entidade Cliente

class Cliente:

    def __init__(self, nome: str, cpf: str):

        self.nome = nome
        self.cpf = cpf
        # Lista vazia para armazenar as contas associadas ao cliente
        self.contas = []

        def adicionar_conta(self, conta):

            # Insere o objeto conta na lista de contas
            self.contas.append(conta)

        # Método especial que define a representação em string do objeto
        def __str__(self):

            # Retorna uma string formatada com nome e CPF do cliente
            return f"Cliente {self.nome} (CPF: {self.cpf})"
