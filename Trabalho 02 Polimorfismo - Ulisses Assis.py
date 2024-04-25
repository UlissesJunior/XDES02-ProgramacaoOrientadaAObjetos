from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @abstractmethod
    def getSalario(self):
        pass


class Horista(EmpDomestica):
    def __init__(self, horasTrabalhadas, valorPorHora):
        self.horasTrabalhadas = horasTrabalhadas
        self.valorPorHora = valorPorHora


    def getSalario(self):
        return self.horasTrabalhadas * self.valorPorHora


class Diarista(EmpDomestica):
    def __init__(self, diasTrabalhados, valorPorDia):
        self.diasTrabalhados = diasTrabalhados
        self.valorPorDia = valorPorDia

    def getSalario(self):
        return self.diasTrabalhados * self.valorPorDia

class Mensalista(EmpDomestica):
    def __init__(self, salarioMensal):
        self.salarioMensal = salarioMensal

    def getSalario(self):
        return self.salarioMensal

def adicionarEmpregados():
    Horista.nome = 'Maria Clara'
    Horista.telefone = '40018911'
    Diarista.nome = 'Priscila'
    Diarista.telefone = '40028922'
    Mensalista.nome = 'Ana Julia'
    Mensalista.telefone = '40038933'

def compararValor():
    adicionarEmpregados()
    empregados = [
        {
            'nome': Horista.nome,
            'telefone': Horista.telefone,
            'salario': Horista(horasTrabalhadas=160, valorPorHora=12).getSalario()
        },
        {
            'nome': Diarista.nome,
            'telefone': Diarista.telefone,
            'salario': Diarista(diasTrabalhados=20, valorPorDia=65).getSalario()
        },
        {
            'nome': Mensalista.nome,
            'telefone': Mensalista.telefone,
            'salario': Mensalista(salarioMensal=1200).getSalario()
        }
    ]
    
    valorMinimo = min([empregado['salario'] for empregado in empregados])
    
    for empregado in empregados:
        if empregado['salario'] == valorMinimo:
            return (f'A empregada {empregado['nome']} tem o melhor valor para a república: R${valorMinimo}, entre em contato com ela pelo telefone {empregado['telefone']}')

print(compararValor())