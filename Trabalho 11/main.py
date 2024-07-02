import tkinter as tk
from tkinter import messagebox
import peixe as est
import comanda as disc
import faturamento as trm

class LimitePrincipal():
    def _init_(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.peixemenu = tk.Menu(self.menubar)
        self.comandaMenu = tk.Menu(self.menubar)
        self.faturatamentoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.peixemenu.add_command(label="Insere", \
                    command=self.controle.inserePeixes)
        self.peixemenu.add_command(label="Mostra", \
                    command=self.controle.mostraPeixes)
        self.menubar.add_cascade(label="Peixe", \
                    menu=self.peixemenu)

        self.comandaMenu.add_command(label="Insere", \
                    command=self.controle.insereDisciplinas)
        self.comandaMenu.add_command(label="Mostra", \
                    command=self.controle.mostraDisciplinas)        
        self.menubar.add_cascade(label="Comanda", \
                    menu=self.comandaMenu)

        self.faturatamentoMenu.add_command(label="Insere", \
                    command=self.controle.insereTurmas)
        self.faturatamentoMenu.add_command(label="Mostra", \
                    command=self.controle.mostraTurmas)                     
        self.menubar.add_cascade(label="Faturamento", \
                    menu=self.faturatamentoMenu)        

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def _init_(self):
        self.root = tk.Tk()

        self.ctrlPeixe = est.CtrlPeixe()
        self.ctrlComanda = disc.CtrlComanda(self)
        self.ctrlFaturamento = trm.CtrlTurma(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def inserePeixes(self):
        self.ctrlPeixe.inserePeixes()

    def mostraPeixes(self):
        self.ctrlPeixe.mostraPeixes()

    def insereComanda(self):
        self.ctrlComanda.insereComanda()

    def mostraComanda(self):
        self.ctrlComanda.mostraComanda()

    def mostraFaturamento(self):
        self.ctrlFaturamento.mostraFaturamento()

    def salvaDados(self):
        self.ctrlPeixe.salvaPeixes()
        #self.ctrlDisciplina.salvaDisciplinas()
        #self.ctrlTurma.salvaTurmas()
        self.root.destroy()

if _name_ == '_main_':
    c = ControlePrincipal()