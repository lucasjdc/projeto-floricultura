import tkinter as tk
def abrir_cadastro(parent):
    cadastro = tk.Toplevel(parent)
    cadastro.title("Cadastro de Produto")
    cadastro.geometry("400x300")
    cadastro.configure(bg='#e0f7fa')

    label = tk.Label(cadastro, text="Cadastro de Produto", font=("Arial", 18, "bold"),
                     bg='#e0f7fa', fg='#006064')
    label.pack(pady=30)

    # Botão para voltar para a janela principal
    btn_voltar = tk.Button(cadastro, text="Voltar", command=cadastro.destroy)
    btn_voltar.pack(pady=10)