class FracaoMista:
    def __init__(self, parte_inteira, numerador, denominador):
        self.parte_inteira = parte_inteira
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        if self.numerador >= self.denominador:
            self.parte_inteira += self.numerador // self.denominador
            self.numerador %= self.denominador
        mdc = self.mdc(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc

    def mdc(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, outra_fracao):
        novo_numerador = self.parte_inteira * self.denominador + self.numerador
        outro_numerador = outra_fracao.parte_inteira * outra_fracao.denominador + outra_fracao.numerador
        denominador_comum = self.denominador * outra_fracao.denominador
        soma_numeradores = novo_numerador * outra_fracao.denominador + outro_numerador * self.denominador
        parte_inteira = soma_numeradores // denominador_comum
        novo_numerador = soma_numeradores % denominador_comum
        return FracaoMista(parte_inteira, novo_numerador, denominador_comum)

    def __str__(self):
        if self.numerador == 0:
            return str(self.parte_inteira)
        elif self.parte_inteira == 0:
            return f"{self.numerador}/{self.denominador}"
        else:
            return f"{self.parte_inteira} {self.numerador}/{self.denominador}"

if __name__ == "__main__":
    f1 = FracaoMista(0, 7, 6)
    f2 = FracaoMista(0, 13, 7)
    print(f"{f1} + {f2} = {f1 + f2}")

    f3 = FracaoMista(0, 1, 3)
    f4 = FracaoMista(0, 2, 3)
    print(f"{f3} + {f4} = {f3 + f4}")

    f5 = FracaoMista(3, 1, 2)
    f6 = FracaoMista(4, 2, 3)
    print(f"{f5} + {f6} = {f5 + f6}")