import tkinter as tk

class Entry():
    def mostrar_entry(self):
        janela = tk.Tk()
        janela.title("Exemplo de Caixa de Entrada")

        entrada = tk.Entry(janela)
        entrada.pack(pady=10)
        
        janela.mainloop()