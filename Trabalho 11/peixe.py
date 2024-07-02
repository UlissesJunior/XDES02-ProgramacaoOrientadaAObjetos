import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Peixe:
    def _init_(self, nome, preco_kg):
        self.__nome = nome
        self.__preco_kg = preco_kg

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco_kg(self):
        return self.__preco_kg  

class LimiteInserePeixes(tk.Toplevel):
    def _init_(self, controle):

        tk.Toplevel._init_(self)
        self.geometry('250x100')
        self.title("Peixe")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelPreco = tk.Label(self.framePreco,text="Preço - KG: ")
        self.labelNome.pack(side="left")  
        self.labelPreco.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraPeixe():
    def _init_(self, str):
        messagebox.showinfo('Lista de peixes', str)
     
class CtrlPeixe():       
    def _init_(self):
        if not os.path.isfile("peixe.pickle"):
            self.listaPeixes =  []
        else:
            with open("peixe.pickle", "rb") as f:
                self.listaPeixes = pickle.load(f)

    def salvaPeixes(self):
        if len(self.listaPeixes) != 0:
            with open("peixe.pickle","wb") as f:
                pickle.dump(self.listaPeixes, f)

    def getPeixe(self, nome):
        pexRet = None
        for pex in self.listaPeixes:
            if pex.nome == nome:
                pexRet = pex
        return pexRet

    def getListanome(self):
        listaPreco = []
        for pex in self.listaPeixes:
            listaPreco.append(pex.nome)
        return listaPreco

    def inserePeixes(self):
        self.limiteIns = LimiteInserePeixes(self) 

    def mostraPeixes(self):
        str = 'Nome -- Preço - KG\n'
        for pex in self.listaPeixes:
            str += pex.nome + ' -- ' + pex.preco_kg + '\n'       
        self.limiteLista = LimiteMostraPeixe(str)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        preco_kg = self.limiteIns.inputPreco.get()
        peixe = Peixe(nome, preco_kg)
        self.listaPeixes.append(peixe)
        self.limiteIns.mostraJanela('Sucesso', 'Peixe cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()