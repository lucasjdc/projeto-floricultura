import tkinter as tk
from cadasdro_produto import abrir_cadastro
from listar_produtos import abrir_lista_produtos


def main():
    root = tk.Tk()
    root.title("Pétala")
    root.geometry("400x300") # Definir tamanho da janela
    root.configure(bg='#f0f0f0') # Cor de fundo

    # Label com melhor formatação
    label = tk.Label(root, text="Pétala", font=("Arial", 24, "bold"),
                     bg='#f0f0f0', fg='#2c3e50')
    label.pack(pady=30)

    # Botão Cadastro
    btn_cadastro = tk.Button(root, text="Cadastro", command=lambda: abrir_cadastro(root))
    btn_cadastro.pack(pady=10)

    # Botão Listar Produtos
    btn_listar = tk.Button(root, text="Listar Produtos", command=lambda: abrir_lista_produtos(root))
    btn_listar.pack(pady=10)

    # Botão Fechar
    btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
    btn_fechar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()