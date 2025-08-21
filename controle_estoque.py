import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class ControleEstoqueFloricultura:
    def __init__(self, root):
        self.root = root
        self.root.title("🌸 Controle de Estoque - Floricultura")
        self.root.geometry("900x600")
        self.root.configure(bg='#f8f6f2')
        
        # Dados do estoque
        self.estoque = []
        self.carregar_estoque()
        
        # Configurar estilo
        self.setup_style()
        
        # Criar interface
        self.criar_interface()
        
    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar cores
        style.configure('TFrame', background='#f8f6f2')
        style.configure('TLabel', background='#f8f6f2', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10), padding=6)
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'), foreground='#4a7c59')
        style.configure('Treeview', font=('Arial', 10))
        style.configure('Treeview.Heading', font=('Arial', 11, 'bold'))
        
    def carregar_estoque(self):
        try:
            if os.path.exists('estoque_floricultura.json'):
                with open('estoque_floricultura.json', 'r', encoding='utf-8') as f:
                    self.estoque = json.load(f)
        except:
            self.estoque = []
    
    def salvar_estoque(self):
        with open('estoque_floricultura.json', 'w', encoding='utf-8') as f:
            json.dump(self.estoque, f, ensure_ascii=False, indent=2)
    
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar expansão
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="🌸 Controle de Estoque - Floricultura", 
                          style='Header.TLabel')
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Formulário de entrada
        form_frame = ttk.LabelFrame(main_frame, text="Adicionar/Editar Item", padding="10")
        form_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        form_frame.columnconfigure(1, weight=1)
        
        # Nome
        ttk.Label(form_frame, text="Nome da Flor/Planta:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.nome_var = tk.StringVar()
        nome_entry = ttk.Entry(form_frame, textvariable=self.nome_var, width=30, font=('Arial', 10))
        nome_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Quantidade
        ttk.Label(form_frame, text="Quantidade:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.quantidade_var = tk.StringVar()
        quantidade_entry = ttk.Entry(form_frame, textvariable=self.quantidade_var, width=10, font=('Arial', 10))
        quantidade_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Categoria
        ttk.Label(form_frame, text="Categoria:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.categoria_var = tk.StringVar()
        categorias = ['Rosas', 'Orquídeas', 'Cactos', 'Plantas Ornamentais', 'Vasos', 'Acessórios', 'Outros']
        categoria_combo = ttk.Combobox(form_frame, textvariable=self.categoria_var, 
                                      values=categorias, state='readonly', width=15)
        categoria_combo.grid(row=2, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Preço
        ttk.Label(form_frame, text="Preço (R$):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.preco_var = tk.StringVar()
        preco_entry = ttk.Entry(form_frame, textvariable=self.preco_var, width=10, font=('Arial', 10))
        preco_entry.grid(row=3, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Botões do formulário
        botoes_frame = ttk.Frame(form_frame)
        botoes_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(botoes_frame, text="➕ Adicionar", command=self.adicionar_item).pack(side=tk.LEFT, padx=5)
        ttk.Button(botoes_frame, text="✏️ Editar", command=self.editar_item).pack(side=tk.LEFT, padx=5)
        ttk.Button(botoes_frame, text="🔄 Atualizar", command=self.atualizar_quantidade).pack(side=tk.LEFT, padx=5)
        ttk.Button(botoes_frame, text="❌ Limpar", command=self.limpar_formulario).pack(side=tk.LEFT, padx=5)
        
        # Frame de pesquisa
        pesquisa_frame = ttk.Frame(main_frame)
        pesquisa_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        pesquisa_frame.columnconfigure(1, weight=1)
        
        ttk.Label(pesquisa_frame, text="Pesquisar:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.pesquisa_var = tk.StringVar()
        pesquisa_entry = ttk.Entry(pesquisa_frame, textvariable=self.pesquisa_var, width=30)
        pesquisa_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        pesquisa_entry.bind('<KeyRelease>', self.filtrar_itens)
        
        ttk.Button(pesquisa_frame, text="🔍", width=3, 
                  command=self.filtrar_itens).grid(row=0, column=2)
        
        # Lista de itens
        lista_frame = ttk.LabelFrame(main_frame, text="Itens em Estoque", padding="10")
        lista_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        lista_frame.columnconfigure(0, weight=1)
        lista_frame.rowconfigure(0, weight=1)
        
        colunas = ("nome", "categoria", "quantidade", "preco", "data_atualizacao")
        self.treeview = ttk.Treeview(lista_frame, columns=colunas, show="headings", height=12)
        
        # Configurar colunas
        self.treeview.heading("nome", text="Nome", anchor=tk.W)
        self.treeview.heading("categoria", text="Categoria", anchor=tk.W)
        self.treeview.heading("quantidade", text="Quantidade", anchor=tk.CENTER)
        self.treeview.heading("preco", text="Preço (R$)", anchor=tk.CENTER)
        self.treeview.heading("data_atualizacao", text="Última Atualização", anchor=tk.CENTER)
        
        self.treeview.column("nome", width=250)
        self.treeview.column("categoria", width=150)
        self.treeview.column("quantidade", width=100)
        self.treeview.column("preco", width=100)
        self.treeview.column("data_atualizacao", width=150)
        
        self.treeview.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(lista_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.treeview.configure(yscrollcommand=scrollbar.set)
        
        # Botões de ação
        acoes_frame = ttk.Frame(main_frame)
        acoes_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        ttk.Button(acoes_frame, text="📊 Estatísticas", 
                  command=self.mostrar_estatisticas).pack(side=tk.LEFT, padx=5)
        ttk.Button(acoes_frame, text="📤 Exportar", 
                  command=self.exportar_dados).pack(side=tk.LEFT, padx=5)
        ttk.Button(acoes_frame, text="💾 Salvar", 
                  command=self.salvar_estoque).pack(side=tk.LEFT, padx=5)
        ttk.Button(acoes_frame, text="🗑️ Remover Selecionado", 
                  command=self.remover_item).pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E))
        
        # Bind para seleção na treeview
        self.treeview.bind('<<TreeviewSelect>>', self.item_selecionado)
        
        # Atualizar a exibição
        self.atualizar_lista()
    
    def adicionar_item(self):
        nome = self.nome_var.get().strip()
        quantidade = self.quantidade_var.get().strip()
        categoria = self.categoria_var.get().strip()
        preco = self.preco_var.get().strip()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, informe o nome do item.")
            return
        
        if not quantidade.isdigit() or int(quantidade) < 0:
            messagebox.showerror("Erro", "Por favor, informe uma quantidade válida.")
            return
        
        # Verificar se item já existe
        for item in self.estoque:
            if item['nome'].lower() == nome.lower():
                messagebox.showerror("Erro", "Este item já existe no estoque.")
                return
        
        novo_item = {
            'nome': nome,
            'quantidade': int(quantidade),
            'categoria': categoria if categoria else 'Outros',
            'preco': float(preco) if preco.replace('.', '').isdigit() else 0.0,
            'data_atualizacao': datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        
        self.estoque.append(novo_item)
        self.atualizar_lista()
        self.limpar_formulario()
        self.status_var.set(f"Item '{nome}' adicionado com sucesso!")
    
    def editar_item(self):
        selecionado = self.treeview.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Por favor, selecione um item para editar.")
            return
        
        item_index = self.treeview.index(selecionado[0])
        nome = self.nome_var.get().strip()
        quantidade = self.quantidade_var.get().strip()
        categoria = self.categoria_var.get().strip()
        preco = self.preco_var.get().strip()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, informe o nome do item.")
            return
        
        if not quantidade.isdigit() or int(quantidade) < 0:
            messagebox.showerror("Erro", "Por favor, informe uma quantidade válida.")
            return
        
        self.estoque[item_index] = {
            'nome': nome,
            'quantidade': int(quantidade),
            'categoria': categoria if categoria else 'Outros',
            'preco': float(preco) if preco.replace('.', '').isdigit() else 0.0,
            'data_atualizacao': datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        
        self.atualizar_lista()
        self.limpar_formulario()
        self.status_var.set(f"Item '{nome}' atualizado com sucesso!")
    
    def atualizar_quantidade(self):
        selecionado = self.treeview.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Por favor, selecione um item para atualizar.")
            return
        
        item_index = self.treeview.index(selecionado[0])
        nova_quantidade = self.quantidade_var.get().strip()
        
        if not nova_quantidade.isdigit():
            messagebox.showerror("Erro", "Por favor, informe uma quantidade válida.")
            return
        
        self.estoque[item_index]['quantidade'] = int(nova_quantidade)
        self.estoque[item_index]['data_atualizacao'] = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        self.atualizar_lista()
        self.status_var.set(f"Quantidade de '{self.estoque[item_index]['nome']}' atualizada para {nova_quantidade}")
    
    def remover_item(self):
        selecionado = self.treeview.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Por favor, selecione um item para remover.")
            return
        
        item_index = self.treeview.index(selecionado[0])
        nome = self.estoque[item_index]['nome']
        
        if messagebox.askyesno("Confirmar", f"Tem certeza que deseja remover '{nome}'?"):
            del self.estoque[item_index]
            self.atualizar_lista()
            self.limpar_formulario()
            self.status_var.set(f"Item '{nome}' removido com sucesso!")
    
    def item_selecionado(self, event):
        selecionado = self.treeview.selection()
        if selecionado:
            item_index = self.treeview.index(selecionado[0])
            item = self.estoque[item_index]
            
            self.nome_var.set(item['nome'])
            self.quantidade_var.set(str(item['quantidade']))
            self.categoria_var.set(item['categoria'])
            self.preco_var.set(str(item['preco']))
    
    def limpar_formulario(self):
        self.nome_var.set("")
        self.quantidade_var.set("")
        self.categoria_var.set("")
        self.preco_var.set("")
    
    def filtrar_itens(self, event=None):
        termo = self.pesquisa_var.get().lower()
        self.atualizar_lista(termo)
    
    def atualizar_lista(self, filtro=None):
        # Limpar treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        # Adicionar itens filtrados
        for item in self.estoque:
            if not filtro or filtro in item['nome'].lower() or filtro in item['categoria'].lower():
                self.treeview.insert("", "end", values=(
                    item['nome'],
                    item['categoria'],
                    item['quantidade'],
                    f"R$ {item['preco']:.2f}",
                    item['data_atualizacao']
                ))
    
    def mostrar_estatisticas(self):
        total_itens = len(self.estoque)
        total_quantidade = sum(item['quantidade'] for item in self.estoque)
        valor_total = sum(item['quantidade'] * item['preco'] for item in self.estoque)
        
        # Contar por categoria
        categorias = {}
        for item in self.estoque:
            categorias[item['categoria']] = categorias.get(item['categoria'], 0) + 1
        
        stats_text = f"""📊 Estatísticas do Estoque:

• Total de itens: {total_itens}
• Quantidade total: {total_quantidade}
• Valor total em estoque: R$ {valor_total:.2f}

📈 Itens por categoria:
"""
        for categoria, quantidade in categorias.items():
            stats_text += f"   • {categoria}: {quantidade} itens\n"
        
        messagebox.showinfo("Estatísticas do Estoque", stats_text)
    
    def exportar_dados(self):
        try:
            with open('estoque_exportado.txt', 'w', encoding='utf-8') as f:
                f.write("Relatório de Estoque - Floricultura\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
                
                for item in self.estoque:
                    f.write(f"Nome: {item['nome']}\n")
                    f.write(f"Categoria: {item['categoria']}\n")
                    f.write(f"Quantidade: {item['quantidade']}\n")
                    f.write(f"Preço: R$ {item['preco']:.2f}\n")
                    f.write(f"Última atualização: {item['data_atualizacao']}\n")
                    f.write("-" * 30 + "\n")
            
            self.status_var.set("Dados exportados para 'estoque_exportado.txt'")
            messagebox.showinfo("Sucesso", "Dados exportados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar dados: {str(e)}")

def main():
    root = tk.Tk()
    app = ControleEstoqueFloricultura(root)
    root.mainloop()

if __name__ == "__main__":
    main()