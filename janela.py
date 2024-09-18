import tkinter as tk

class JanelaTkinter():
    def visualizar_janela(self):
        janela = tk.Tk()
        janela.title("Janela Principal")
        janela.geometry("400x400")
        
        janela.mainloop()