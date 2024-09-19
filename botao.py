import tkinter as tk

class BotaoTkinter():
    def ao_clicar(self):
        print("Botão Clicado")

    janela = tk.Tk()
    janela.title("Exemplo de Botão")

    botao = tk.Button(janela, text="Clique-me", command=ao_clicar)
    botao.pack(pady=10)

    janela.mainloop()
