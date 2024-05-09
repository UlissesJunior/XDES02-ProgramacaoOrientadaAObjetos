from abc import ABC, abstractmethod

class FolhaDePagamento(ABC):
    def __init__(self, codigo, nome, pontoMensalFunc):
        self.codigo = codigo
        self.nome = nome
        self.pontoMensalFunc = pontoMensalFunc
    
    @property
    def getCodigo(self):
        return self.codigo
    
    @property
    def getNome(self):
        return self.nome
    
    @property
    def getPontoMensalFunc(self):
        return self.pontoMensalFunc
    
    def adicionaPonto(self, mes, ano, nroFaltas, nroAtrasos):
        self.pontoMensalFunc = PontoFunc(mes, ano, nroFaltas, nroAtrasos)
        
    def lancaFaltas(self, mes, ano, nroFaltas):
        self.pontoMensalFunc.lancaFaltas(nroFaltas)
    
    def lancaAtrasos(self, mes, ano, nroAtrasos):
        self.pontoMensalFunc.lancaAtrasos(nroAtrasos)
        
    def imprimeFolha(self, mes, ano):
        print(f'Código: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'Salário líquido: {self.calculaSalario(mes, ano):.2f}')
        print(f'Bonus: {self.calculaBonus(mes, ano):.2f}')

class Professor(FolhaDePagamento):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome, pontoMensalFunc=None)
        self.titulacao = titulacao
        self.salarioHora = salarioHora
        self.nroAulas = nroAulas
        
    @property
    def getTitulacao(self):
        return self.titulacao
    
    @property
    def getSalarioHora(self):
        return self.salarioHora
    
    @property
    def getNroAulas(self):
        return self.nroAulas
    
    def calculaSalario(self, mes, ano):
        return self.salarioHora * self.nroAulas - self.salarioHora * self.pontoMensalFunc.getNroFaltas

    def calculaBonus(self, mes, ano):
        atrasos = self.pontoMensalFunc.getNroAtrasos
        bonus = 0.1 - 0.01 * atrasos
        return bonus * self.calculaSalario(mes, ano)
        
class TecAdmin(FolhaDePagamento):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome,  pontoMensalFunc=None)
        self.funcao = funcao
        self.salarioMensal = salarioMensal
        
    @property
    def getFuncao(self):
        return self.funcao
    
    @property
    def getSalarioMensal(self):
        return self.salarioMensal
    
    def calculaSalario(self, mes, ano):
        return self.salarioMensal - ((self.salarioMensal / 30) * self.pontoMensalFunc.getNroFaltas)
        
    def calculaBonus(self, mes, ano):
        atrasos = self.pontoMensalFunc.getNroAtrasos
        bonus = 0.08 - 0.01 * atrasos
        return bonus * self.calculaSalario(mes, ano)

class PontoFunc(FolhaDePagamento):
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.mes = mes
        self.ano = ano
        self.nroFaltas = nroFaltas
        self.nroAtrasos = nroAtrasos
    
    @property
    def getMes(self):
        return self.mes
    
    @property
    def getAno(self):
        return self.ano
    
    @property
    def getNroFaltas(self):
        return self.nroFaltas
    
    @property
    def getNroAtrasos(self):
        return self.nroAtrasos
    
    def lancaFaltas(self, nroFaltas):
        self.nroFaltas += nroFaltas
        
    def lancaAtrasos(self, nroAtrasos):
        self.nroAtrasos += nroAtrasos
    
if __name__ == "__main__":
    funcionarios = []
    
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()