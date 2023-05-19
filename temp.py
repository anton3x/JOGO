import tkinter as tk


class BoardGameGUI:
    def __init__(self, master):
        self.master = master
        self.movements = []

        # define a fonte e o tamanho do texto
        self.font = ('Arial', 14)

        # cria a caixa de texto
        self.text_box = tk.Text(master, height=10, width=40, font=self.font,
                                bg='#F5F5F5', padx=10, pady=10, wrap='word')
        self.text_box.tag_config('player_move', font=self.font, foreground='blue')
        self.text_box.tag_config('opponent_move', font=self.font, foreground='red')
        self.text_box.pack(fill='both', expand=True)

        # adiciona um exemplo de movimento
        self.add_movement('Player move: e2-e4', 'player_move')
        self.add_movement('Opponent move: e7-e5', 'opponent_move')

    def add_movement(self, movement_text, tag):
        self.text_box.insert(tk.END, movement_text + "\n", tag)
        self.movements.append(movement_text)


root = tk.Tk()
board_game_gui = BoardGameGUI(root)
root.mainloop()