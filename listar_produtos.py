import tkinter as tk
from tkinter import ttk, messagebox
import json

def abrir_lista_produtos(parent):
    lista = tk.Toplevel(parent)
    lista.title("Lista de Produtos")
    lista.geometry("800x500")
    lista.configure(bg='#e0f7fa')

    label = tk.Label(lista, text="Lista de Produtos", font=("Arial", 18, "bold"), bg='#e0f7fa', fg='#006064')
    label.pack(pady=10)

    # Frame para a tabela
    frame_tabela = tk.Frame(lista)
    frame_tabela.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Criar a tabela
    colunas = ("nome", "quantidade", "preco", "data", "descricao")
    tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

    # Definir os cabeçalhos
    tabela.heading("nome", text="Nome")
    tabela.heading("quantidade", text="Quantidade")
    tabela.heading("preco", text="Preço")
    tabela.heading("data", text="Data")
    tabela.heading("descricao", text="Descrição")

    # Definir a largura das colunas
    tabela.column("nome", width=150)
    tabela.column("quantidade", width=80)
    tabela.column("preco", width=80)
    tabela.column("data", width=100)
    tabela.column("descricao", width=200)

    # Adicionar scrollbar
    scrollbar = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tabela.yview)
    tabela.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Carregar produtos
    try:
        with open("produtos.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)

        for produto in produtos:
            # Formatar o preço para exibição
            preco_formatado = f"R$ {float(produto['preco']):.2f}"
            # Usar get() para evitar KeyError com descrição
            descricao = produto.get('descricao', '-')

            tabela.insert("", tk.END, values=(
                produto['nome'],
                produto['quantidade'],
                preco_formatado,
                produto['data'],
                descricao
            ))
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo("Informação", "Nenhum produto cadastrado ainda.")
        lista.destroy()
        return
    
    # Botão Voltar
    btn_voltar = tk.Button(lista, text="Voltar", command=lista.destroy, bg="#00796b", fg="white")
    btn_voltar.pack(pady=10)

    