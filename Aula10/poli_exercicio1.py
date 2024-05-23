from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    def calculaValorImposto(self, salBruto):
        if salBruto < 1903.9:
            imposto = 0
        elif salBruto < 2826.66:
            imposto = 7.5
        elif salBruto < 3751.06:
            imposto = 15
        elif salBruto < 4664.68:
            imposto = 22.5
        else:
            imposto = 27.5
        return (salBruto * imposto)/100

    @abstractmethod
    def calculaSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    @property
    def salarioBruto(self):
        return self.__salarioBruto

    @salarioBruto.setter
    def salarioBruto(self, sal):
        self.__salarioBruto = sal

    @salarioLiquido.setter
    def salarioLiquido(self, x):
        self.__salarioLiquido = x

    def calculaSalario(self):
        print(self.__salarioBruto)
        previd = self.__salarioBruto * 0.11
        imposto = self.calculaValorImposto(self.__salarioBruto)
        return self.__salarioBruto - (previd + imposto)        

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora

    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def calculaSalario(self):
        salBruto = self.__salarioHora * self.cargaHoraria
        imposto = self.calculaValorImposto(salBruto)
        return salBruto - imposto

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    prof1.salarioBruto = 6000    


    prof1.salarioLiquido = f()

    prof2.salarioHora = 85

    profs = [prof1, prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário líquido: {}'.format(prof.nome, prof.calculaSalario()))


          

