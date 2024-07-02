import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Peixe:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    

class LimiteInserePeixe(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Cadastrar Peixe")
        self.controle = controle
        
        self.frameNome = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack(pady=7)
        self.framePreco.pack()
        self.frameButton.pack(pady=7)

        self.labelNome = tk.Label(self.frameNome, text="Nome: ", width=10)
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelPreco = tk.Label(self.framePreco, text="Preço: ", width=10)
        self.labelPreco.pack(side="left")
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Cadastrar")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.HandlerInserePeixe)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.HandlerLimpaInsere)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.HandlerConcluiInsere)


class CtrlPeixe:
    def __init__(self, controle):
        self.CtrlPrincipal = controle
        self.listaPeixes = []

    def InserePeixe(self):
        self.limiteIns = LimiteInserePeixe(self)

    def MostraPeixe(self):

        string = 'Nome - Preço por Kg\n'
        for peixe in self.listaPeixes:
            string += str(peixe.nome) + ' - R$' + str(peixe.preco) + '\n'
        self.MostraMensagem("Peixes Cadastrados", string)

    def HandlerInserePeixe(self, event):
        nomeSel = self.limiteIns.inputNome.get()
        try: precoSel = float(self.limiteIns.inputPreco.get())
        except:
            self.MostraMensagem("Erro", "Preço inválido")
            return

        peixe = Peixe(nomeSel, precoSel)
        self.listaPeixes.append(peixe)
        self.MostraMensagem("Sucesso", "Peixe Cadastrado")
        self.HandlerLimpaInsere(event)


    def HandlerLimpaInsere(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))

    def HandlerConcluiInsere(self, event):
        self.limiteIns.destroy()
    
    def GetListaNomesPeixes(self):
        nomes = []
        for peixe in self.listaPeixes:
            nomes.append(peixe.nome)
        return nomes
    
    def MostraMensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
