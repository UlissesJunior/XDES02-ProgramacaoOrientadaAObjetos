
import tkinter as tk
from tkinter import messagebox
import Peixe
import Comanda

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.peixeMenu = tk.Menu(self.menubar)
        self.comandaMenu = tk.Menu(self.menubar)
        self.relatorioMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.peixeMenu.add_command(label="Cadastra", command=self.controle.InserePeixe)
        self.peixeMenu.add_command(label="Mostra", command=self.controle.MostraPeixe)
        self.menubar.add_cascade(label="Peixe", menu=self.peixeMenu)

        self.comandaMenu.add_command(label="Fechamento", command=self.controle.InsereComanda)
        self.menubar.add_cascade(label="Comanda", menu=self.comandaMenu)

        self.relatorioMenu.add_command(label="Faturamento", command=self.controle.Relatorio)
        self.menubar.add_cascade(label="Relatorio", menu=self.relatorioMenu)

        self.root.config(menu=self.menubar)
    
    
class CtrlPrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlPeixe = Peixe.CtrlPeixe(self)
        self.ctrlComanda = Comanda.CtrlComanda(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Pesque-Pague MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def InserePeixe(self):
        self.ctrlPeixe.InserePeixe()

    def MostraPeixe(self):
        self.ctrlPeixe.MostraPeixe()

    def InsereComanda(self):
        self.ctrlComanda.InsereComanda()

    def Relatorio(self):
        self.ctrlComanda.Relatorio()


if __name__ == '__main__':
    c = CtrlPrincipal()