import tkinter as tk
from tkinter import ttk

def iniciar_jogo():
    jogador1 = entry_jogador1.get()
    jogador2 = entry_jogador2.get()
    variante = dropdown_variante.get()
    print("Jogador 1:", jogador1)
    print("Jogador 2:", jogador2)
    print("Variante escolhida:", variante)

janela = tk.Tk()
janela.title("Jogo")

label_jogador1 = tk.Label(janela, text="Jogador 1:")
label_jogador1.grid(column=0, row=0)
entry_jogador1 = tk.Entry(janela)
entry_jogador1.grid(column=1, row=0)

label_jogador2 = tk.Label(janela, text="Jogador 2:")
label_jogador2.grid(column=0, row=1)
entry_jogador2 = tk.Entry(janela)
entry_jogador2.grid(column=1, row=1)

label_variante = tk.Label(janela, text="Variante:")
label_variante.grid(column=0, row=2)
dropdown_variante = ttk.Combobox(janela, values=["Normal", "Do Bruno"])
dropdown_variante.grid(column=1, row=2)
dropdown_variante.current(0)

botao_iniciar = tk.Button(janela, text="Começar Jogo", command=iniciar_jogo)
botao_iniciar.grid(column=1, row=3)

janela.mainloop()