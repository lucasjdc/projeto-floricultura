import tkinter as tk

# cria a janela
root = tk.Tk()
root.title("Olá, mundo!")

# adiciona um rótulo
label = tk.Label(root, text="Olá, mundo!")
label.pack(padx=20, pady=20)

# inicia o loop da interface
root.mainloop()