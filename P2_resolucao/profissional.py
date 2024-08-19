import tkinter as tk
from tkinter import messagebox

#Model
class Profissional():
    def __init__(self, cpf, nome, email, valorPilates, valorFuncional):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__valorPilates = valorPilates
        self.__valorFuncional = valorFuncional

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
    def valorPilates(self):
        return self.__valorPilates
    
    @property
    def valorFuncional(self):
        return self.__valorFuncional
    

#View
class LimiteInserePro(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.title("Cadastrar Profissional")
        self.geometry("300x150")

        self.controlador = controlador

        self.frameCpf = tk.Frame(self)
        self.frameCpf.pack()
        self.frameNome = tk.Frame(self)
        self.frameNome.pack()
        self.frameEmail = tk.Frame(self)
        self.frameEmail.pack()
        self.frameVP = tk.Frame(self)
        self.frameVP.pack()
        self.frameVF = tk.Frame(self)
        self.frameVF.pack()

        self.labelCpf = tk.Label(self.frameCpf, text = "CPF: ")
        self.labelCpf.pack(side = "left")
        self.labelNome = tk.Label(self.frameNome, text = "Nome: ")
        self.labelNome.pack(side = "left")
        self.labelEmail = tk.Label(self.frameEmail, text = "E-mail: ")
        self.labelEmail.pack(side = "left")
        self.labelVP = tk.Label(self.frameVP, text = "Valor Pilates: ")
        self.labelVP.pack(side = "left")
        self.labelVF = tk.Label(self.frameVF, text = "Valor Funcional: ")
        self.labelVF.pack(side = "left")

        self.entryCpf = tk.Entry(self.frameCpf, width=20)
        self.entryCpf.pack(side = "left")
        self.entryNome = tk.Entry(self.frameNome, width=20)
        self.entryNome.pack(side = "left")
        self.entryEmail = tk.Entry(self.frameEmail, width=20)
        self.entryEmail.pack(side = "left")
        self.entryVP = tk.Entry(self.frameVP, width=20)
        self.entryVP.pack(side = "left")
        self.entryVF = tk.Entry(self.frameVF, width=20)
        self.entryVF.pack(side = "left")

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

class LimiteMostraPro():
    def __init__(self, controlador):
        self.controlador = controlador
    
    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteFaturaPro(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.title("Faturamento do Profissional")
        self.geometry("300x380")

        self.controlador = controlador

        self.frameCpf = tk.Frame(self)
        self.frameCpf.pack()
        self.frameText = tk.Frame(self)
        self.frameText.pack()

        self.labelCpf = tk.Label(self.frameCpf, text = "CPF do profissional: ")
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
class CtrlPro():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.lista = []
    
    def getNomes(self):
        nomes = []
        for i in self.lista:
            nomes.append(i.nome)
        return nomes
    
    def getObj(self, nome):
        ret = None
        for i in self.lista:
            if i.nome == nome:
                ret = i
        return ret

    def inserePro(self):
        self.limiteIns = LimiteInserePro(self)
    
    def cadastra(self, event):
        cpf = self.limiteIns.entryCpf.get()
        nome = self.limiteIns.entryNome.get()
        email = self.limiteIns.entryEmail.get()
        vp = float(self.limiteIns.entryVP.get())
        vf = float(self.limiteIns.entryVF.get())
        prof = Profissional(cpf, nome, email, vp, vf)
        self.lista.append(prof)
        self.limiteIns.mostraJanela("Sucesso", "Profissional cadastrado com sucesso.")
        self.limpa(event)        
    
    def limpa(self, event):
        self.limiteIns.entryCpf.delete(0, len(self.limiteIns.entryCpf.get()))
        self.limiteIns.entryNome.delete(0, len(self.limiteIns.entryNome.get()))
        self.limiteIns.entryEmail.delete(0, len(self.limiteIns.entryEmail.get()))
        self.limiteIns.entryVP.delete(0, len(self.limiteIns.entryVP.get()))
        self.limiteIns.entryVF.delete(0, len(self.limiteIns.entryVF.get()))
    
    def listaPro(self):
        self.limiteMos = LimiteMostraPro(self)
        mensagem = ""
        for i in self.lista:
            mensagem += f"Nome: {i.nome}\nCPF: {i.cpf}\nE-mail: {i.email}\nValor Pilates: {i.valorPilates}\nValor Funcional: {i.valorFuncional}\n----------\n"
        if not mensagem:
            mensagem = "Não há nenhum profissional cadastrado."
        self.limiteMos.mostraJanela("Profissionais Cadastrados", mensagem)
    
    def faturaPro(self):
        self.limiteFat = LimiteFaturaPro(self)
    
    def atualiza(self, event):
        cpf = self.limiteFat.entryCpf.get()
        obj = None
        for i in self.lista:
            if i.cpf == cpf:
                obj = i
        self.limiteFat.text.config(state = tk.NORMAL)
        self.limiteFat.text.delete("1.0", tk.END)
        if obj:
            alunos = self.ctrlPrincipal.ctrlAlu.getAlunos()
            valorP = 0
            valorF = 0
            for i in alunos:
                if i.professor.nome == obj.nome:
                    if i.nAula == "2 aulas":
                        mul = 0
                    elif i.nAula == "3 aulas":
                        mul = 0.4
                    else:
                        mul = 0.8
                    if i.tipo == "Pilates":
                        valorP += obj.valorPilates + (obj.valorPilates * mul)
                    else:
                        valorF += obj.valorFuncional + (obj.valorFuncional * mul)
            self.limiteFat.text.insert(tk.END, f"Profissional {obj.nome}\nValor Pilates: {valorP}\nValor Funcional: {valorF}\nValor Total: {valorP + valorF}")
        else:
            self.limiteFat.text.insert(tk.END, "Profissional não encontrado!")
        self.limiteFat.text.config(state=tk.DISABLED)

    def fecha1(self, event):
        self.limiteIns.destroy()

    def fecha2(self, event):
        self.limiteFat.destroy()      


    
