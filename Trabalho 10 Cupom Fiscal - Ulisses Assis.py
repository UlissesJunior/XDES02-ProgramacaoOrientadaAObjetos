import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import pickle
import os

class Produto:
    def __init__(self, codigo, descricao, valor_unitario):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor_unitario

    def __str__(self):
        return f"Código: {self.codigo}, Descrição: {self.descricao}, Valor Unitário: R${self.valor_unitario:.2f}"

class CupomFiscal:
    def __init__(self, nroCupom):
        self.nroCupom = nroCupom
        self.itensCupom = []

    def adicionar_item(self, produto):
        self.itensCupom.append(produto)

    def fechar_cupom(self):
        pass

    def __str__(self):
        produtos_agrupados = {}
        for produto in self.itensCupom:
            if produto.codigo in produtos_agrupados:
                produtos_agrupados[produto.codigo]['quantidade'] += 1
            else:
                produtos_agrupados[produto.codigo] = {'produto': produto, 'quantidade': 1}

        resultado = f"Cupom Fiscal Nº: {self.nroCupom}\n"
        total = 0.0
        for item in produtos_agrupados.values():
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal = quantidade * produto.valor_unitario
            resultado += f"{produto.descricao} - {quantidade} x R${produto.valor_unitario:.2f} = R${subtotal:.2f}\n"
            total += subtotal
        resultado += f"Total: R${total:.2f}"
        return resultado

class LojaConveniencia:
    def __init__(self, root):
        self.root = root
        self.root.title("Loja de Conveniência")

        self.produtos = {}
        self.cupons = {}

        self.load_data()

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        menu_produto = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Produto", menu=menu_produto)
        menu_produto.add_command(label="Cadastrar", command=self.cadastrar_produto)
        menu_produto.add_command(label="Consultar", command=self.consultar_produto)

        menu_cupom = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Cupom Fiscal", menu=menu_cupom)
        menu_cupom.add_command(label="Criar", command=self.criar_cupom_fiscal)
        menu_cupom.add_command(label="Consultar", command=self.consultar_cupom_fiscal)

    def cadastrar_produto(self):
        codigo = simpledialog.askinteger("Cadastro de Produto", "Código:")
        descricao = simpledialog.askstring("Cadastro de Produto", "Descrição:")
        valor_unitario = simpledialog.askfloat("Cadastro de Produto", "Valor Unitário:")

        if codigo and descricao and valor_unitario:
            produto = Produto(codigo, descricao, valor_unitario)
            self.produtos[codigo] = produto
            self.save_data()
            messagebox.showinfo("Cadastro de Produto", "Produto cadastrado com sucesso!")
        else:
            messagebox.showwarning("Cadastro de Produto", "Todos os campos são obrigatórios!")

    def consultar_produto(self):
        codigo = simpledialog.askinteger("Consulta de Produto", "Código do Produto:")
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            messagebox.showinfo("Consulta de Produto", str(produto))
        else:
            messagebox.showwarning("Consulta de Produto", "Produto não encontrado!")

    def criar_cupom_fiscal(self):
        nroCupom = simpledialog.askinteger("Criar Cupom Fiscal", "Número do Cupom Fiscal:")
        if not nroCupom:
            return

        cupom = CupomFiscal(nroCupom)

        produtos_lista = [str(produto) for produto in self.produtos.values()]
        selecionado = tk.StringVar()
        combo = ttk.Combobox(self.root, textvariable=selecionado, values=produtos_lista)

        def adicionar_produto():
            for produto in self.produtos.values():
                if str(produto) == selecionado.get():
                    cupom.adicionar_item(produto)
                    messagebox.showinfo("Adicionar Produto", "Produto adicionado ao cupom!")
                    break

        def fechar_cupom():
            self.cupons[nroCupom] = cupom
            self.save_data()
            messagebox.showinfo("Cupom Fiscal", f"Cupom fiscal criado:\n{cupom}")
            combo.destroy()
            add_button.destroy()
            close_button.destroy()

        combo.pack()
        add_button = tk.Button(self.root, text="Adicionar Produto", command=adicionar_produto)
        add_button.pack()
        close_button = tk.Button(self.root, text="Fechar Cupom", command=fechar_cupom)
        close_button.pack()

    def consultar_cupom_fiscal(self):
        nroCupom = simpledialog.askinteger("Consultar Cupom Fiscal", "Número do Cupom Fiscal:")
        if nroCupom in self.cupons:
            cupom = self.cupons[nroCupom]
            messagebox.showinfo("Consultar Cupom Fiscal", str(cupom))
        else:
            messagebox.showwarning("Consultar Cupom Fiscal", "Cupom não encontrado!")

    def save_data(self):
        with open("produtos.pkl", "wb") as f:
            pickle.dump(self.produtos, f)
        with open("cupons.pkl", "wb") as f:
            pickle.dump(self.cupons, f)

    def load_data(self):
        if os.path.exists("produtos.pkl"):
            with open("produtos.pkl", "rb") as f:
                self.produtos = pickle.load(f)
        if os.path.exists("cupons.pkl"):
            with open("cupons.pkl", "rb") as f:
                self.cupons = pickle.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = LojaConveniencia(root)
    root.mainloop()