import tkinter as tk
from tkinter import messagebox
import profissional
import aluno

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.profissionalMenu = tk.Menu(self.menubar)
        self.alunoMenu = tk.Menu(self.menubar)

        self.profissionalMenu.add_command(label="Cadastra", \
                    command=self.controle.cadastraProfissional)
        self.profissionalMenu.add_command(label="Lista", \
                    command=self.controle.mostraProfissional)
        self.profissionalMenu.add_command(label="Faturamento", \
                    command=self.controle.mostraFaturamento)
        self.menubar.add_cascade(label="Profissional", \
                    menu=self.profissionalMenu)
        
        self.alunoMenu.add_command(label="Cadastra", \
                    command=self.controle.insereAluno)
        self.alunoMenu.add_command(label="Lista", \
                    command=self.controle.mostraAluno)
        self.menubar.add_cascade(label="Alunos", \
                    menu=self.alunoMenu)
        
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProfissional = profissional.CtrlProfissional(self)
        self.ctrlAluno = aluno.CtrlAluno(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Gestão de Estúdio")
        self.root.mainloop()
       
    def cadastraProfissional(self):
        self.ctrlProfissional.cadastraProfissional()

    def mostraProfissional(self):
        self.ctrlProfissional.mostraProfissional()

    def mostraFaturamento(self):
        self.ctrlProfissional.mostraFaturamento()
        
    def insereAluno(self):
        self.ctrlAluno.insereAluno()

    def mostraAluno(self):
        self.ctrlAluno.mostraAluno()


if __name__ == '__main__':
    c = ControlePrincipal()