from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, codigo, nome, vendas):
        self.codigo = codigo
        self.nome = nome
        self.vendas = vendas
        
    @property
    def getCodigo(self):
        return self.codigo
    
    @property
    def getVendas(self):
        return self.vendas
    
    @property
    def getNome(self):
        return self.nome
    
    def adicionaVenda(self, pCodImovel, pMes, pAno, pValor):
        self.vendas.append(Venda(pCodImovel, pMes, pAno, pValor))
        
    @abstractmethod
    def getDados(self):
        pass
    
    @abstractmethod
    def calculaRenda(self, pMes, pAno):
        pass


class Venda():
    def __init__(self, pCodImovel, pMesVenda, pAnoVenda, pValorVenda):
        self.codImovel = pCodImovel
        self.mes = pMesVenda
        self.ano = pAnoVenda
        self.valor = pValorVenda
        
    @property
    def getCodImovel(self):
        return self.codImovel
    
    @property
    def getMesVenda(self):
        return self.mes
    
    @property
    def getAnoVenda(self):
        return self.ano
    
    @property
    def getValorVenda(self):
        return self.valor
    
     
class Contratado(Vendedor):
    def __init__(self, pCodigo, Nome, PSalario, pNroCartTrabalho):
        super().__init__(pCodigo, Nome, [])
        self.salario = PSalario
        self.nroCartTrabalho = pNroCartTrabalho
        
    @property
    def getNroCartTrabalho(self):
        return self.nroCartTrabalho
    
    @property
    def getSalarioFixo(self):
        return self.salario
     
    def getDados(self):
        return f'Nome: {self.nome} - Nro Carteira: {self.nroCartTrabalho}'
    
    def calculaRenda(self, pMes, pAno):
        total = 0
        for venda in self.vendas:
            if venda.getMesVenda == pMes and venda.getAnoVenda == pAno:
                total += 0.01 * venda.getValorVenda
        return total + self.salario
        
    
class Comissionado(Vendedor):
    def __init__(self, pCodigo, Nome, pNroCPF, pComissao):
        super().__init__(pCodigo, Nome, [])
        self.nroCPF = pNroCPF
        self.comissao = pComissao
        
    @property
    def getNroCPF(self):
        return self.nroCPF
    
    @property
    def getComissao(self):
        return self.comissao
    
    def getDados(self):
        return f'Nome: {self.nome} - Nro CPF: {self.nroCPF}'
    
    def calculaRenda(self, pMes, pAno):
        total = 0
        bonus = 0.01 * self.comissao
        for venda in self.vendas:
            if venda.getMesVenda == pMes and venda.getAnoVenda == pAno:
                total += bonus * venda.getValorVenda
        return total
        

if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))