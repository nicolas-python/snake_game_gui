#snake

import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

class snake_game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.root.geometry("400x400")

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack()

        self.button_create_player = tk.Button(self.frame_buttons, text="Spieler erstellen",command=self.create_player)
        self.button_create_player.pack(pady=10)

        self.button_select_player = tk.Button(self.frame_buttons, text="Spieler wählen",command=self.select_player)
        self.button_select_player.pack(pady=10)

        self.button_play = tk.Button(self.frame_buttons, text="Spielen", command=self.play)
        self.button_play.pack(pady=10)

        self.button_score = tk.Button(self.frame_buttons, text="Score anzeigen", command=self.score)
        self.button_score.pack(pady=10)

        self.button_exit = tk.Button(self.frame_buttons, text="Beenden", command=self.exit_game)
        self.button_exit.pack(pady=10)

        self.root.mainloop()

    def create_player(self):
        print("Spieler wird erstellt")
    def select_player(self):
        print("Spieler aussuchen")
    def play(self):
        print("play")
    def score(self):
        print("score")
    def exit_game(self):
        self.root.destroy()


snake_game()