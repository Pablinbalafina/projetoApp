import tkinter as tk

class Rotulo():
    def visualizar_rotulo(self):
        janela =tk.Tk()
        janela.title("Exemplo de Rotulo")

        label = tk.label(janela, text="Este é um rotulo")
        label.pack(pady=10)

        janela.mainloop()