import tkinter as tk

# cria a janela principal
root = tk.Tk()
root.title("Pétala")

# adiciona um label
label = tk.Label(root, text="Pétala", font=("Arial", 16, "bold"))
label.pack(padx=20, pady=20)

# adicion um botão para fechar o app
btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
btn_fechar.pack(padx=20, pady=10)

# inicia o loop da interface
root.mainloop()