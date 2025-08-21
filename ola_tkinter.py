import tkinter as tk
from tkinter import messagebox

# cria a janela
root = tk.Tk()
root.title("Exemplo tkinter")

def dizer_oi():
    messagebox.showinfo("Mensagem", "Olá, mundo!")

btn = tk.Button(root, text="Clique aqui", command=dizer_oi)
btn.pack(padx=20, pady=20)

# inicia o loop da interface
root.mainloop()