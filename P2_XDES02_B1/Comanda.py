
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Comanda:
    def __init__(self, nomes, pesos, custos):
        self._nomes = nomes
        self._pesos = pesos
        self._custos = custos

    @property
    def nomes(self):
        return self._nomes
    
    @property
    def pesos(self):
        return self._pesos
    
    @property
    def custos(self):
        return self._custos
    

class LimiteInsereComanda(tk.Toplevel):
    def __init__(self, controle, peixes):
        tk.Toplevel.__init__(self)
        self.geometry('450x100')
        self.title("Cadastrar Comanda")
        self.controle = controle
        
        self.frameNome = tk.Frame(self)
        self.framePeso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack(pady=7)
        self.framePeso.pack()
        self.frameButton.pack(pady=7)

        self.labelNome = tk.Label(self.frameNome, text="Nome: ", width=10)
        self.labelNome.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.inputNome = ttk.Combobox(self.frameNome, width = 18, textvariable = self.escolhaCombo)
        self.inputNome['values'] = peixes
        self.inputNome.pack(side="left")

        self.labelPeso = tk.Label(self.framePeso, text="Peso: ", width=10)
        self.labelPeso.pack(side="left")
        self.inputPeso = tk.Entry(self.framePeso, width=20)
        self.inputPeso.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Adicionar Peixe")           
        self.buttonInsere.pack(side="left", padx=4)
        self.buttonInsere.bind("<Button>", controle.HandlerInserePeixe)

        self.buttonInsere = tk.Button(self.frameButton ,text="Fecha Comanda")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.HandlerFechaComanda)

        self.buttonLimpa = tk.Button(self.frameButton ,text="Limpar")           
        self.buttonLimpa.pack(side="left", padx=4)
        self.buttonLimpa.bind("<Button>", controle.HandlerLimpaInsere)

        self.buttonConclui = tk.Button(self.frameButton ,text="Concluir")           
        self.buttonConclui.pack(side="left")
        self.buttonConclui.bind("<Button>", controle.HandlerConcluiInsere)


class CtrlComanda:
    def __init__(self, controle):
        self.CtrlPrincipal = controle
        self.listaPeixes = []
        self.listaComandas = []

    def InsereComanda(self):
        peixes = self.CtrlPrincipal.ctrlPeixe.GetListaNomesPeixes()
        self.limiteIns = LimiteInsereComanda(self, peixes)

    def HandlerInserePeixe(self, event):
        nomeSel = self.limiteIns.inputNome.get()
        pesoSel = self.limiteIns.inputPeso.get()
        peixes = self.CtrlPrincipal.ctrlPeixe.GetListaPeixes()

        for peixe in peixes:
            if(peixe.nome == nomeSel):
                try:
                    custo = float(pesoSel)*float(peixe.preco)
                    self.listaPeixes.append([nomeSel, float(pesoSel), custo])
                except:
                    self.MostraMensagem("Erro", "Peso inválido")
                    return
                    
        self.MostraMensagem("Sucesso", "Peixe Adicionado")
        self.HandlerLimpaInsere(event)

    def HandlerFechaComanda(self, event):
        if(self.listaPeixes == []):
            self.MostraMensagem("Erro", "É preciso adicionar pelo menos um peixe")
            return

        nomes = []
        pesos = []
        custos = []

        for peixe in self.listaPeixes:
            nomes.append(peixe[0])
            pesos.append(peixe[1])
            custos.append(peixe[2])
        
        self.listaPeixes = []
        comanda = Comanda(nomes, pesos, custos)
        self.listaComandas.append(comanda)

        string = "Nome - Quantidade - Preço\n"
        for i in range(len(nomes)):
            string += str(nomes[i]) + ' - ' + str(pesos[i]) + 'Kg - R$' + str(custos[i]) + '\n'
        string += 'Total: R$' + str(round(sum(custos), 2))
        self.MostraMensagem("Resumo da Comanda", string)
        self.HandlerLimpaInsere(event)

    def HandlerLimpaInsere(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputPeso.delete(0, len(self.limiteIns.inputPeso.get()))

    def HandlerConcluiInsere(self, event):
        self.limiteIns.destroy()

    def Relatorio(self):
        totais = {}
        comandas = self.listaComandas

        for comanda in comandas:
            for i in range(len(comanda.nomes)):
                try:
                    totais[comanda.nome[i]][0] += comanda.peso[i]
                    totais[comanda.nome[i]][1] += comanda.custo[i]
                except:
                    totais[comanda.nome[i]] = [comanda.peso[i], comanda.custo[i]]
        
        total = 0
        string = 'Nome - Quantidade - Preço\n'
        for peixe in totais:
            string += str(peixe) + ' - ' + str(totais[peixe][0]) + 'Kg - R$' + str(totais[peixe][1]) + '\n'
            total += totais[peixe][1]
        total = round(total, 2)
        string += 'Total: R$' + str(total)
        self.MostraMensagem('Faturamento por tipo de peixe', string)

    def MostraMensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg)