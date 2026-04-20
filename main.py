#snake

import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

from player import create_player as cp

class snake_game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.root.geometry("400x400")

        #menü
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(expand=True)

        self.button_create_player = tk.Button(self.frame_buttons, text="Spieler erstellen",command=self.show_create_player)
        self.button_create_player.pack(pady=10)

        self.button_select_player = tk.Button(self.frame_buttons, text="Spieler wählen",command=self.select_player)
        self.button_select_player.pack(pady=10)

        self.button_play = tk.Button(self.frame_buttons, text="Spielen", command=self.play)
        self.button_play.pack(pady=10)

        self.button_score = tk.Button(self.frame_buttons, text="Score anzeigen", command=self.score)
        self.button_score.pack(pady=10)

        self.button_exit = tk.Button(self.frame_buttons, text="Beenden", command=self.exit_game)
        self.button_exit.pack(pady=10)

        #creat player
        self.frame_create_player = tk.Frame(self.root)
        cp(self.frame_create_player)

        back_button = tk.Button(self.frame_create_player, text="Zurück", command=self.show_menu)
        back_button.pack(pady=10)

        #select player

        self.root.mainloop()

    def show_create_player(self):
        self.frame_buttons.pack_forget()
        self.frame_create_player.pack(expand=True, fill="both")

    def show_menu(self):
        self.frame_create_player.pack_forget()
        self.frame_buttons.pack(expand=True)

    def select_player(self):
        print("Spieler aussuchen")
    def play(self):
        print("play")
    def score(self):
        print("score")
    def exit_game(self):
        self.root.destroy()


snake_game()