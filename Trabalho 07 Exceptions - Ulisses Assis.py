class Pessoa:
    def __init__(self, nome, endereço, idade, cpf):
        self.nome = nome
        self.endereço = endereço
        self.idade = idade
        self.cpf = cpf

    @property
    def getNome(self):
        return self.nome
    
    @property
    def getEndereço(self):
        return self.endereço
    
    @property
    def getIdade(self):
        return self.idade
    
    @property
    def getCpf(self):
        return self.cpf
    
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereço, idade, cpf, titulacao):
        super().__init__(nome, endereço, idade, cpf)
        self.titulacao = titulacao
        
    @property  
    def getTitulacao(self):
        return self.titulacao

    def printDescricao(self):
        print(f"Professor: {self.nome}")
        print(f"Endereço: {self.endereço}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Titulação: {self.titulacao}")

class Aluno(Pessoa):
    def __init__(self, nome, endereço, idade, cpf, curso):
        super().__init__(nome, endereço, idade, cpf)
        self.curso = curso

    @property
    def getCurso(self):
        return self.curso
    
    def printDescricao(self):
        print(f"Aluno: {self.nome}")
        print(f"Endereço: {self.endereço}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Curso: {self.curso}")

def cadastrar_pessoa(pessoa):
    if any(p.cpf == pessoa.cpf for p in pessoas):
        raise Exception("CPF já cadastrado")

    if isinstance(pessoa, Professor):
        if pessoa.titulacao != "doutor":
            raise Exception(f"Titulação inválida do professor {pessoa.nome}")
        if pessoa.idade < 30:
            raise Exception(f"Idade mínima não atendida para professor {pessoa.nome}")
    elif isinstance(pessoa, Aluno):
        if pessoa.curso not in ["CCO", "SIN"]:
            raise Exception(f"Curso inválido do aluno {pessoa.nome}")
        if pessoa.idade < 18:
            raise Exception(f"Idade mínima não atendida para aluno {pessoa.nome}")

    pessoas.append(pessoa)

pessoas = []

erros = []

try:
    pessoa = Professor(nome="João", endereço="Rua A", idade=35, cpf="12345678901", titulacao="doutor")
    cadastrar_pessoa(pessoa)
except Exception as e:
    erros.append(str(e))

try:
    pessoa = Aluno(nome="Maria", endereço="Rua B", idade=20, cpf="12345678902", curso="CCO")
    cadastrar_pessoa(pessoa)
except Exception as e:
    erros.append(str(e))

try:
    pessoa = Aluno(nome="José", endereço="Rua C", idade=17, cpf="12345678903", curso="SIN")
    cadastrar_pessoa(pessoa)
except Exception as e:
    erros.append(str(e))

try:
    pessoa = Aluno(nome="Ana", endereço="Rua D", idade=17, cpf="12345678904", curso="SIN")
    cadastrar_pessoa(pessoa)
except Exception as e:
    erros.append(str(e))

try:
    pessoa = Professor(nome="Pedro", endereço="Rua E", idade=29, cpf="12345678905", titulacao="mestre")
    cadastrar_pessoa(pessoa)
except Exception as e:
    erros.append(str(e))

for erro in erros:
    print(f"Erro ao cadastrar pessoa: {erro}")

for pessoa in pessoas:
    pessoa.printDescricao()
    print()