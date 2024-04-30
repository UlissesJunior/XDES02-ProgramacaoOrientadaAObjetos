from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, nomeCorrentista, numeroConta, saldoConta=0):
        self.nomeCorrentista = nomeCorrentista
        self.numeroConta = numeroConta
        self.saldoConta = saldoConta
        self._extrato = []  
    
    @property
    def extrato(self):
        return self._extrato
    
    def deposito(self, data, valor, descricao):
        self._extrato.append({'data': data, 'valor': valor, 'descricao': descricao})
        self.saldoConta += valor

    @abstractmethod
    def retirada(self, data, valor, descricao):
        pass
    
    @abstractmethod
    def imprimirExtrato(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, nomeCorrentista, numeroConta, saldoConta=0):
        super().__init__(nomeCorrentista, numeroConta, saldoConta)

    def retirada(self, data, valor, descricao):
        self._extrato.append({'data': data, 'valor': -valor, 'descricao': descricao})
        self.saldoConta -= valor
    
    def imprimirExtrato(self):
        return self._extrato, self.saldoConta

class ContaCorrenteComLimite(Conta):
    def __init__(self, nomeCorrentista, numeroConta, saldoConta=0, limite=0):
        super().__init__(nomeCorrentista, numeroConta, saldoConta)
        self.limite = limite
    
    def retirada(self, data, valor, descricao):
        if self.saldoConta + self.limite < valor:
            return "Saldo insuficiente"
        self._extrato.append({'data': data, 'valor': -valor, 'descricao': descricao})
        self.saldoConta -= valor
    
    def imprimirExtrato(self):
        return self._extrato, self.limite, self.saldoConta

class ContaPoupanca(Conta):
    def __init__(self, nomeCorrentista, numeroConta, saldoConta=0, aniversario=""):
        super().__init__(nomeCorrentista, numeroConta, saldoConta)
        self.aniversario = aniversario

    def retirada(self, data, valor, descricao):
        if self.saldoConta < valor:
            return "Saldo insuficiente"
        self._extrato.append({'data': data, 'valor': -valor, 'descricao': descricao})
        self.saldoConta -= valor
        
    def imprimirExtrato(self):
        return self._extrato, self.aniversario, self.saldoConta

         
contas = []

conta1 = ContaCorrente(nomeCorrentista="João", numeroConta=123, saldoConta=1000)
conta1.deposito(data="01/01/2021", valor=100, descricao="Depósito em dinheiro")
conta1.deposito(data="02/01/2021", valor=200, descricao="Depósito em dinheiro")
conta1.retirada(data="03/01/2021", valor=50, descricao="Saque em dinheiro")
contas.append(conta1)

conta2 = ContaCorrenteComLimite(nomeCorrentista="Maria", numeroConta=456, saldoConta=2000, limite=1000)
conta2.deposito(data="01/01/2022", valor=100, descricao="Depósito em dinheiro")
conta2.deposito(data="02/01/2022", valor=200, descricao="Depósito em dinheiro")
conta2.retirada(data="03/01/2022", valor=50, descricao="Saque em dinheiro")
contas.append(conta2)

conta3 = ContaPoupanca(nomeCorrentista="José", numeroConta=789, saldoConta=3000, aniversario="01/01")
conta3.deposito(data="01/01/2024", valor=100, descricao="Depósito em dinheiro")
conta3.deposito(data="02/01/2024", valor=200, descricao="Depósito em dinheiro")
conta3.retirada(data="03/01/2024", valor=50, descricao="Saque em dinheiro")
contas.append(conta3)

for conta in contas:
    print(conta.imprimirExtrato())