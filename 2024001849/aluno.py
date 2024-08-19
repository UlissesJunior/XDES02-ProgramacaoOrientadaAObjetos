import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog

class Aluno:
    def __init__(self, nome, email, cpf, tipoAula, nomeProfessor, numeroAulas):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__tipoAula = tipoAula
        self.__nomeProfessor = nomeProfessor
        self.__numeroAulas = numeroAulas

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
    def tipoAula(self):
        return self.__tipoAula
    
    @property
    def nomeProfessor(self):
        return self.__nomeProfessor
    
    @property
    def numeroAulas(self):
        return self.__numeroAulas
    
class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle, listaNomeProf):

        tk.Toplevel.__init__(self)
        self.geometry('300x170')
        self.title("Cadastro de Aluno")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameCpf = tk.Frame(self)
        self.frameTipoAula = tk.Frame(self)
        self.frameNomeProfessor = tk.Frame(self)
        self.frameNumeroAulas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameNome.pack()
        self.frameEmail.pack()
        self.frameCpf.pack()
        self.frameTipoAula.pack()
        self.frameNomeProfessor.pack()
        self.frameNumeroAulas.pack()
        self.frameButton.pack()     

        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelEmail = tk.Label(self.frameEmail,text="Email: ")
        self.labelEmail.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")

        self.labelCpf = tk.Label(self.frameCpf,text="CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCpf, width=20)
        self.inputCpf.pack(side="left")

        listaTiposAula = ["Pilates", "Funcional"]
        self.labelTipoAula = tk.Label(self.frameTipoAula,text="Escolha o Tipo de Aula: ")
        self.labelTipoAula.pack(side="left")
        self.escolhaComboTipos = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameTipoAula, width = 15 , textvariable = self.escolhaComboTipos)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaTiposAula
          
        self.labelNomeProfessor = tk.Label(self.frameNomeProfessor,text="Escolha o Professor: ")
        self.labelNomeProfessor.pack(side="left")
        self.escolhaComboProfessores = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameNomeProfessor, width = 15 , textvariable = self.escolhaComboProfessores)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeProf

        listaNumeroAulas = [2, 3, 4]
        self.labelNumeroAulas = tk.Label(self.frameNumeroAulas,text="Escolha o Número de aulas: ")
        self.labelNumeroAulas.pack(side="left")
        self.escolhaComboAulas = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameNumeroAulas, width = 15 , textvariable = self.escolhaComboAulas)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNumeroAulas

        self.buttonInsere = tk.Button(self.frameButton ,text="Inserir")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.criaAluno)

        self.buttonClear = tk.Button(self.frameButton ,text="Limpar")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.limpaForm)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaJanela)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg) 

class LimiteMostraAlunos():
    def __init__(self, titulo, corpo):
        messagebox.showinfo(titulo, corpo)

class CtrlAluno:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunos = []

    def insereAluno(self):        
        listaNomesProfissional = self.ctrlPrincipal.ctrlProfissional.getListaNomeProfissional()
        self.limiteIns = LimiteInsereAluno(self, listaNomesProfissional)     
    
    def criaAluno(self, event):
        nome = self.limiteIns.inputNome.get()
        email = self.limiteIns.inputEmail.get()
        cpf = self.limiteIns.inputCpf.get()
        tipoAula = self.limiteIns.escolhaComboTipos.get()
        nomeProfessor = self.limiteIns.escolhaComboProfessores.get()
        numeroAulas = self.limiteIns.escolhaComboAulas.get()

        try:
            aluno = Aluno(nome, email, cpf, tipoAula, nomeProfessor, numeroAulas)
            self.listaAlunos.append(aluno)            
            self.limiteIns.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
            self.limpaForm(event)
        except ValueError as error:
            self.limiteIns.mostraJanela('Erro', error)  

    def limpaForm(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
        self.limiteIns.inputCpf.delete(0, len(self.limiteIns.inputCpf.get()))
        self.limiteIns.escolhaComboTipos.set('')
        self.limiteIns.escolhaComboProfessores.set('') 
        self.limiteIns.escolhaComboAulas.set('') 

    def listaTodosAlunos(self):
        return self.listaAlunos

    def mostraAluno(self):
        codigoConsulta = simpledialog.askstring("Consultar Aluno", "Digite o CPF do aluno:")
        alunoEncontrado = next((cliente for cliente in self.listaAlunos if cliente.cpf == codigoConsulta), None)
        
        if alunoEncontrado:
            mensalidade = self.mostraMensalidade(alunoEncontrado, alunoEncontrado.nomeProfessor, alunoEncontrado.tipoAula)
            messagebox.showinfo('Aluno Encontrado', 
                                f'Nome: {alunoEncontrado.nome}\n'+
                                f'Email: {alunoEncontrado.email}\n'+
                                f'CPF: {alunoEncontrado.cpf}\n'+
                                f'Tipo de Aula: {alunoEncontrado.tipoAula}\n'+
                                f'Nome do Professor: {alunoEncontrado.nomeProfessor}\n'+
                                f'Numero de Aulas: {alunoEncontrado.numeroAulas}\n'+
                                f'Mensalidade: {mensalidade}'
                                )
                        
        else:
            messagebox.showinfo('Erro', 'Código não cadastrado')

    def mostraMensalidade(self, aluno, professor, tipoAula):
        mensalidadeProfissional = self.ctrlPrincipal.ctrlProfissional.getListaMensalidadeProfissional(professor, tipoAula)
        if(aluno.numeroAulas == "4"):
            mensalidadeProfessor = mensalidadeProfissional + ((mensalidadeProfissional/100)*80)
            return mensalidadeProfessor + ((mensalidadeProfessor/100)*50)
        elif(aluno.numeroAulas == "3"):
            mensalidadeProfessor = mensalidadeProfissional + ((mensalidadeProfissional/100)*40)
            return  mensalidadeProfessor + ((mensalidadeProfessor/100)*50)
        elif(aluno.numeroAulas == "2"):
            return mensalidadeProfissional + ((mensalidadeProfissional/100)*50)


    def fechaJanela(self, event):
        self.limiteIns.destroy()