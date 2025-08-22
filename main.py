import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pétala")
root.geometry("400x300") # Definir tamanho da janela
root.configure(bg='#f0f0f0') # Cor de fundo

# Label com melhor formatação
label = tk.Label(root, text="Pétala", font=("Arial", 24, "bold"),
                 bg='#f0f0f0', fg='#2c3e50')
label.pack(pady=30)

# Botão com estilo melhorado
btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
btn_fechar.pack(pady=10)

# inicia o loop da interface
root.mainloop()