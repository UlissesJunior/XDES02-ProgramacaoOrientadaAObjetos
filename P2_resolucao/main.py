
import tkinter as tk
import profissional as pro
import aluno as al

#View
class LimitePrincipal():
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = self.controlador.root
        self.root.title("XDES02 - Prova 2")
        self.root.geometry("300x250")

        self.menubar = tk.Menu(self.root)
        self.menuPro = tk.Menu(self.menubar)
        self.menuAlu = tk.Menu(self.menubar)

        self.menuPro.add_command(label="Cadastra", command=self.controlador.inserePro)
        self.menuPro.add_command(label="Lista", command=self.controlador.listaPro)
        self.menuPro.add_command(label = "Faturamento", command=self.controlador.faturaPro)
        self.menubar.add_cascade(label="Profissional", menu = self.menuPro)

        self.menuAlu.add_command(label="Cadastra", command=self.controlador.insereAlu)
        self.menuAlu.add_command(label="Consulta", command=self.controlador.consultaAlu)
        self.menubar.add_cascade(label="Aluno", menu = self.menuAlu)

        self.root.config(menu = self.menubar)

#Controlador
class CtrlPrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlPro = pro.CtrlPro(self)
        self.ctrlAlu = al.CtrlAlu(self)

        self.view = LimitePrincipal(self)

        self.root.mainloop()
    
    def inserePro(self):
        self.ctrlPro.inserePro()

    def listaPro(self):
        self.ctrlPro.listaPro()
    
    def faturaPro(self):
        self.ctrlPro.faturaPro()

    def insereAlu(self):
        self.ctrlAlu.insereAlu()
    
    def consultaAlu(self):
        self.ctrlAlu.consultaAlu()

if __name__ == "__main__":
    CtrlPrincipal()