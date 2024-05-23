class Veiculo:

    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    @property
    def marca(self):
        return self.__marca
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def motorLigado(self):
        return self.__motorLigado
    
    def ligaMotor(self):
        if self.__motorLigado == True:
            print('Motor já está ligado')
        else:
            self.__motorLigado = True
            print('Motor acaba de ser ligado')

class Carro(Veiculo):

    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio

    @property
    def portaMalasCheio(self):
        return self.__portaMalasCheio
    
    def enchePortaMalas(self):
        if(self.__portaMalasCheio == True):
            print('Porta malas já está cheio')
        else:
            self.__portaMalasCheio = True
            print('O porta malas agora está cheio')

    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.marca, self.cor))
        if (self.motorLigado == True):
            print('Seu motor está ligado.')
        else:
            print('Seu motor está desligado.')
        if (self.portaMalasCheio == True):
            print('Seu porta malas está cheio.')
        else:
            print('Seu porta malas está vazio.')            

class Motocicleta(Veiculo):

    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    @property
    def estilo(self):
        return self.__estilo
    
    def mostraAtributos(self):
        print('Esta é uma {} {} {}'.format(self.marca, self.cor, self.estilo))
        if (self.motorLigado == True):
            print('Seu motor está ligado.')
        else:
            print('Seu motor está desligado.')        
    
if __name__=='__main__':
    m = Motocicleta('Honda','azul','False','naked')
    m.mostraAtributos()
    m.ligaMotor()
    m.mostraAtributos()
    print('----------')
    c = Carro('Chevrolet','branco',False,False)
    c.mostraAtributos()
    c.enchePortaMalas()
    c.ligaMotor()
    c.mostraAtributos()


