import tkinter as tk
from tkinter import messagebox, ttk

#Model
class Aluno():
    def __init__(self, cpf, nome, email, tipo, professor, nAula, fatura):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__tipo = tipo
        self.__professor = professor
        self.__nAula = nAula
        self.__fatura = fatura
    
    @property
    def cpf(self):
        return self.__cpf
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def professor(self):
        return self.__professor
    
    @property
    def nAula(self):
        return self.__nAula
    
    @property
    def fatura(self):
        return self.__fatura
    
#View
class LimiteInsereAlu(tk.Toplevel):
    def __init__(self, controlador, professores):
        tk.Toplevel.__init__(self)
        self.title("Cadastrar Alunos")
        self.geometry("300x150")

        self.controlador = controlador

        self.tipos = ["Pilates", "Funcional"]
        self.qnt = ["2 aulas", "3 aulas", "4 aulas"]

        self.frameCpf = tk.Frame(self)
        self.frameCpf.pack()
        self.frameNome = tk.Frame(self)
        self.frameNome.pack()
        self.frameEmail = tk.Frame(self)
        self.frameEmail.pack()
        self.frameTipo = tk.Frame(self)
        self.frameTipo.pack()
        self.framePro = tk.Frame(self)
        self.framePro.pack()
        self.frameQnt = tk.Frame(self)
        self.frameQnt.pack()

        self.labelCpf = tk.Label(self.frameCpf, text = "CPF: ")
        self.labelCpf.pack(side = "left")
        self.labelNome = tk.Label(self.frameNome, text = "Nome: ")
        self.labelNome.pack(side = "left")
        self.labelEmail = tk.Label(self.frameEmail, text = "E-mail: ")
        self.labelEmail.pack(side = "left")
        self.labelTipo = tk.Label(self.frameTipo, text = "Seleciona a aula: ")
        self.labelTipo.pack(side = "left")
        self.labelPro = tk.Label(self.framePro, text = "Selecione o professor: ")
        self.labelPro.pack(side = "left")
        self.labelQnt = tk.Label(self.frameQnt, text = "Selecione a quantidade: ")
        self.labelQnt.pack(side = "left")

        self.entryCpf = tk.Entry(self.frameCpf, width=20)
        self.entryCpf.pack(side = "left")
        self.entryNome = tk.Entry(self.frameNome, width=20)
        self.entryNome.pack(side = "left")
        self.entryEmail = tk.Entry(self.frameEmail, width=20)
        self.entryEmail.pack(side = "left")

        self.escolhaTipo = tk.StringVar()
        self.comboTipo = ttk.Combobox(self.frameTipo, values=self.tipos, width=10, textvariable=self.escolhaTipo)
        self.comboTipo.pack(side = "left")

        self.escolhaPro = tk.StringVar()
        self.comboPro = ttk.Combobox(self.framePro, values=professores, width=10, textvariable=self.escolhaPro)
        self.comboPro.pack(side = "left")

        self.escolhaQnt = tk.StringVar()
        self.comboQnt = ttk.Combobox(self.frameQnt, values=self.qnt, width=10, textvariable=self.escolhaQnt)
        self.comboQnt.pack(side = "left")
        
        self.buttonInsere = tk.Button(self, text = "Cadastrar")
        self.buttonInsere.pack(side = "left")
        self.buttonInsere.bind("<Button>", self.controlador.cadastra)

        self.buttonLimpa = tk.Button(self, text = "Limpar")
        self.buttonLimpa.pack(side = "left")
        self.buttonLimpa.bind("<Button>", self.controlador.limpa)

        self.buttonFecha = tk.Button(self, text = "Concluído")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", self.controlador.fecha1)

    def mostraJanela(self, titulo, mensagem):
        if titulo == "Error":
            messagebox.showerror(titulo, mensagem)
        else:
            messagebox.showinfo(titulo, mensagem)

class LimiteMostraAlu(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.title("Consultar Alunos")
        self.geometry("300x380")

        self.controlador = controlador

        self.frameCpf = tk.Frame(self)
        self.frameCpf.pack()
        self.frameText = tk.Frame(self)
        self.frameText.pack()

        self.labelCpf = tk.Label(self.frameCpf, text = "CPF do aluno: ")
        self.labelCpf.pack(side = "left")

        self.entryCpf = tk.Entry(self.frameCpf, width=20)
        self.entryCpf.pack(side="left")

        self.text = tk.Text(self.frameText, height=15, width=30)
        self.text.pack()
        self.text.config(state = tk.DISABLED)

        self.buttonConsulta = tk.Button(self, text = "Consultar")
        self.buttonConsulta.pack(side = "left")
        self.buttonConsulta.bind("<Button>", self.controlador.atualiza)

        self.buttonFecha = tk.Button(self, text = "Concluído")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", self.controlador.fecha2)

#Controlador
class CtrlAlu():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.lista = []
    
    def getAlunos(self):
        return self.lista

    def getObj(self, cpf):
        ret = None
        for i in self.lista:
            if i.cpf == cpf:
                ret = i
        return ret

    def insereAlu(self):
        nomes = self.ctrlPrincipal.ctrlPro.getNomes()
        self.limiteIns = LimiteInsereAlu(self, nomes)
    
    def cadastra(self, event):
        cpf = self.limiteIns.entryCpf.get()
        nome = self.limiteIns.entryNome.get()
        email = self.limiteIns.entryEmail.get()
        tipo = self.limiteIns.escolhaTipo.get()
        pro = self.limiteIns.escolhaPro.get()
        qnt = self.limiteIns.escolhaQnt.get()

        obj = self.ctrlPrincipal.ctrlPro.getObj(pro)

        if obj:
            if tipo == "Pilates":
                valor = obj.valorPilates
            else:
                valor = obj.valorFuncional

            if qnt == "3 aulas":
                valor += valor * 0.4
            elif qnt == "4 aulas":
                valor += valor * 0.8
            valor += valor * 0.5

            aluno = Aluno(cpf, nome, email, tipo, obj, qnt, valor)
            self.lista.append(aluno)
            self.limiteIns.mostraJanela("Sucesso", "Aluno cadastrado com sucesso.")
            self.limpa(event)
        else:
            self.limiteIns.mostraJanela("Error", "Professor inválido.")

    
    def limpa(self, event):
        self.limiteIns.entryCpf.delete(0, len(self.limiteIns.entryCpf.get()))
        self.limiteIns.entryNome.delete(0, len(self.limiteIns.entryNome.get()))
        self.limiteIns.entryEmail.delete(0, len(self.limiteIns.entryEmail.get()))
        self.limiteIns.comboPro.set("...")
        self.limiteIns.comboTipo.set("...")
        self.limiteIns.comboQnt.set("...")


    def consultaAlu(self):
        self.limiteMos = LimiteMostraAlu(self)
    
    def atualiza(self, event):
        cpf = self.limiteMos.entryCpf.get()

        obj = self.getObj(cpf)

        self.limiteMos.text.config(state = tk.NORMAL)
        self.limiteMos.text.delete("1.0", tk.END)
        if obj:
            self.limiteMos.text.insert(tk.END, f"Nome: {obj.nome}\nCPF: {obj.cpf}\nE-mail: {obj.email}\nAulas: {obj.nAula}\nProfessor: {obj.professor.nome}\nTipo: {obj.tipo}\n")
            self.limiteMos.text.insert(tk.END, f"\nMensalidade: {obj.fatura}")
        else:
            self.limiteMos.text.insert(tk.END, "Aluno não encontrado!")
        self.limiteMos.text.config(state = tk.DISABLED)

    def fecha1(self, event):
        self.limiteIns.destroy()

    def fecha2(self, event):
        self.limiteMos.destroy()     
    