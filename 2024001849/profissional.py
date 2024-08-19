import tkinter as tk
from tkinter import messagebox, simpledialog

class Profissional:

    def __init__(self, nome, email, cpf, valorPilates, valorFuncional):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__valorPilates = valorPilates
        self.__valorFuncional = valorFuncional

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def valorPilates(self):
        return self.__valorPilates
    
    @property
    def valorFuncional(self):
        return self.__valorFuncional
    

class LimiteCadastraProfissional(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadastrar Profissional")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameCpf = tk.Frame(self)
        self.frameValorPilates = tk.Frame(self)
        self.frameValorFuncional = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameNome.pack()
        self.frameEmail.pack()
        self.frameCpf.pack()
        self.frameValorPilates.pack()
        self.frameValorFuncional.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelCpf = tk.Label(self.frameCpf, text="Cpf: ")
        self.labelValorPilates = tk.Label(self.frameValorPilates, text="Valor Pilates: ")
        self.labelValorFuncional = tk.Label(self.frameValorFuncional, text="Valor Funcional: ")

        self.labelNome.pack(side="left")  
        self.labelEmail.pack(side="left")
        self.labelCpf.pack(side="left")
        self.labelValorPilates.pack(side="left")
        self.labelValorFuncional.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCpf, width=20)
        self.inputCpf.pack(side="left")
        self.inputValorPilates = tk.Entry(self.frameValorPilates, width=20)
        self.inputValorPilates.pack(side="left")
        self.inputValorFuncional = tk.Entry(self.frameValorFuncional, width=20)
        self.inputValorFuncional.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Inserir")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
        self.buttonClear = tk.Button(self.frameButton ,text="Limpar")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  
        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteListaProfissional():
    def __init__(self, str):
        messagebox.showinfo('Lista de Profissionais', str)
      
class CtrlProfissional():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaProfissional = [
            Profissional('Ulisses', 'gmail', '1', 100, 120)
        ]

    def getProfissional(self, nome):
        profissionalRent = None
        for profissional in self.listaProfissional:
            if profissional.nome == nome:
                profissionalRent = profissional
        return profissionalRent
    
    def getListaNomeProfissional(self):
        listaNome = []
        for profissional in self.listaProfissional:
            listaNome.append(profissional.nome)
        return listaNome
    
    def getListaMensalidadeProfissional(self, nome, tipoAula):
        for profissional in self.listaProfissional:
            if profissional.nome == nome:
                if tipoAula == "Pilates":
                    return profissional.valorPilates
                elif tipoAula == "Funcional":
                    return profissional.valorFuncional

    def cadastraProfissional(self):
        self.limiteIns = LimiteCadastraProfissional(self) 

    def mostraProfissional(self):
        str = ''
        for profissional in self.listaProfissional:
            str += f'Nome: {profissional.nome} \n'
            str += f'Email: {profissional.email} \n' 
            str += f'CPF: {profissional.cpf} \n'       
            str += f'Valor Pilates: {profissional.valorPilates} \n'       
            str += f'Valor Funcional: {profissional.valorFuncional} \n'
            str += '\n---- \n\n'       

        self.limiteLista = LimiteListaProfissional(str)

    def mostraFaturamento(self):
        codigoConsulta = simpledialog.askstring("Consultar Faturamento", "Digite o CPF do Profissional:")
        profissionalEncontrado = next((profissional for profissional in self.listaProfissional if profissional.cpf == codigoConsulta), None)
        
        faturamentoPilates = 0
        faturamentoFuncional = 0

        if profissionalEncontrado:
            alunos = self.ctrlPrincipal.ctrlAluno.listaTodosAlunos()
            for aluno in alunos:
                if(profissionalEncontrado.nome == aluno.nomeProfessor):
                    if(aluno.tipoAula == "Pilates"):
                        if(aluno.numeroAulas == "4"):
                            mensalidadeProfessor = profissionalEncontrado.valorPilates + ((profissionalEncontrado.valorPilates/100)*80)
                            faturamentoPilates += mensalidadeProfessor
                        elif(aluno.numeroAulas == "3"):
                            mensalidadeProfessor = profissionalEncontrado.valorPilates + ((profissionalEncontrado.valorPilates/100)*40)
                            faturamentoPilates += mensalidadeProfessor
                        elif(aluno.numeroAulas == "2"):
                            faturamentoPilates += profissionalEncontrado.valorPilates
                    elif(aluno.tipoAula == "Funcional"):
                        if(aluno.numeroAulas == "4"):
                            mensalidadeProfessor = profissionalEncontrado.valorFuncional + ((profissionalEncontrado.valorFuncional/100)*80)
                            faturamentoFuncional += mensalidadeProfessor
                        elif(aluno.numeroAulas == "3"):
                            mensalidadeProfessor = profissionalEncontrado.valorFuncional + ((profissionalEncontrado.valorFuncional/100)*40)
                            faturamentoFuncional += mensalidadeProfessor
                        elif(aluno.numeroAulas == "2"):
                            faturamentoFuncional += profissionalEncontrado.valorFuncional

        messagebox.showinfo('Faturamento do Profissional', 
                            f'Valor Pilates: {faturamentoPilates}\n'+
                            f'Valor Funcional: {faturamentoFuncional}'
                            )
                    

            
    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        email = self.limiteIns.inputEmail.get()
        cpf = self.limiteIns.inputCpf.get()
        valorPilates = float(self.limiteIns.inputValorPilates.get())
        valorFuncional = float(self.limiteIns.inputValorFuncional.get())
        profissional = Profissional(nome, email, cpf, valorPilates, 
                                    valorFuncional)
        self.listaProfissional.append(profissional)
        self.limiteIns.mostraJanela('Sucesso', 'Profissional cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
        self.limiteIns.inputCpf.delete(0, len(self.limiteIns.inputCpf.get()))
        self.limiteIns.inputValorPilates.delete(0, len(self.limiteIns.inputValorPilates.get()))
        self.limiteIns.inputValorFuncional.delete(0, len(self.limiteIns.inputValorFuncional.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()