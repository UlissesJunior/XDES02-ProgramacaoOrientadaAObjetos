import tkinter as tk
from tkinter import messagebox

class Orientador:

    def __init__(self, email, nome):
        self.__email = email
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @property
    def nome(self):
        return self.__nome

class LimiteInsereOrientadores(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Orientador")
        self.controle = controle

        self.frameEmail = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameEmail.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelNome.pack(side="left")  
        self.labelEmail.pack(side="left")

        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
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

class LimiteMostraOrientadores():
    def __init__(self, str):
        messagebox.showinfo('Lista de Orientadores', str)
      
class CtrlOrientador():       
    def __init__(self):
        self.listaOrientadores = [
            Orientador('ulisses@unifei.edu.br', 'Ulisses'),
            Orientador('jose@unifei.edu.br', 'Jose'),
            Orientador('ana@unifei.edu.br', 'Ana'),
        ]

    def getOrientador(self, nome):
        orientRet = None
        for orientador in self.listaOrientadores:
            if orientador.nome == nome:
                orientRet = orientador
        return orientRet
    
    def getListaNomeOrient(self):
        listaNome = []
        for orientador in self.listaOrientadores:
            listaNome.append(orientador.nome)
        return listaNome

    def insereOrientador(self):
        self.limiteIns = LimiteInsereOrientadores(self) 

    def mostraOrientador(self):
        str = 'Email | Nome\n'
        for orientador in self.listaOrientadores:
            str += f'{orientador.nome} | {orientador.email}\n'       
        self.limiteLista = LimiteMostraOrientadores(str)

    def enterHandler(self, event):
        email = self.limiteIns.inputEmail.get()
        nome = self.limiteIns.inputNome.get()
        orientador = Orientador(email, nome)
        self.listaOrientadores.append(orientador)
        self.limiteIns.mostraJanela('Sucesso', 'Orientador cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    