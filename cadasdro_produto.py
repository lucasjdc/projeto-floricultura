import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
from produto import Produto

def abrir_cadastro(parent):
    cadastro = tk.Toplevel(parent)
    cadastro.title("Cadastro de Produto")
    cadastro.geometry("400x400")
    cadastro.configure(bg='#e0f7fa')

    label = tk.Label(cadastro, text="Cadastro de Produto", font=("Arial", 18, "bold"),
                     bg='#e0f7fa', fg='#006064')
    label.pack(pady=10)

    # Campos de entrada
    tk.Label(cadastro, text="Nome:", bg="#e0f7fa").pack()
    entry_nome = tk.Entry(cadastro)
    entry_nome.pack()

    tk.Label(cadastro, text="Quantidade:", bg='#e0f7fa').pack()
    entry_qtd = tk.Entry(cadastro)
    entry_qtd.pack()

    tk.Label(cadastro, text="Preço", bg='#e0f7fa').pack()
    entry_preco = tk.Entry(cadastro)
    entry_preco.pack()

    tk.Label(cadastro, text="Data (dd/mm/aaaa):", bg='#e0f7fa').pack()
    entry_data = tk.Entry(cadastro)
    entry_data.pack()

    tk.Label(cadastro, text="Descrição (opcional):", bg='#e0f7fa').pack()
    entry_desc = tk.Entry(cadastro)
    entry_desc.pack()

    def salvar():
        nome = entry_nome.get().strip()
        qtd = entry_qtd.get().strip()
        preco = entry_preco.get().strip()
        data = entry_data.get().strip()
        desc = entry_desc.get().strip()

        try:
            produto = Produto(
                nome=nome,
                quantidade=qtd,
                preco=preco,
                data=data,
                descricao=desc if desc else None                
            )
        
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            return

        # Salvar no arquivo JSON
        try:
            with open("produtos.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = []
        
        dados.append(produto.dict())

        with open("produtos.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        cadastro.destroy()

    # Botão
    btn_salvar = tk.Button(cadastro, text="Salvar", command=salvar, bg="#00796b", fg="white")
    btn_salvar.pack(pady=10)


    btn_voltar = tk.Button(cadastro, text="Voltar", command=cadastro.destroy)
    btn_voltar.pack(pady=10)

