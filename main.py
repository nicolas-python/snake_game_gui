#snake

import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

from player import create_player as cp
from player import select_player as sp
from database import init_db
from database import save_player

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

        self.button_select_player = tk.Button(self.frame_buttons, text="Spieler wählen",command=self.show_select_player)
        self.button_select_player.pack(pady=10)

        self.button_play = tk.Button(self.frame_buttons, text="Spielen", command=self.play)
        self.button_play.pack(pady=10)

        self.button_score = tk.Button(self.frame_buttons, text="Score anzeigen", command=self.score)
        self.button_score.pack(pady=10)

        self.button_exit = tk.Button(self.frame_buttons, text="Beenden", command=self.exit_game)
        self.button_exit.pack(pady=10)

        #creat player
        self.frame_create_player = tk.Frame(self.root)
        self.entry = cp(self.frame_create_player)

        self.back_button_create = tk.Button(self.frame_create_player, text="Zurück", command=self.show_menu)
        self.back_button_create.pack(pady=10)

        self.save_button_create = tk.Button(self.frame_create_player,text="Speichern",command=self.create_player_save)
        self.save_button_create.pack(pady=10)

        #select player
        self.frame_select_player = tk.Frame(self.root)
        self.listbox = sp(self.frame_select_player)

        self.save_button_select = tk.Button(self.frame_select_player, text="Auswählen", command=self.select_player_save)
        self.save_button_select.pack(pady=10)

        self.back_button_select = tk.Button(self.frame_select_player, text="Zurück", command=self.show_menu_1)
        self.back_button_select.pack(pady=10)

        self.root.mainloop()

    def create_player_save(self):
        name = self.entry.get()
        save_player(name)

    def show_create_player(self):
        self.frame_buttons.pack_forget()
        self.frame_create_player.pack(expand=True, fill="both")

    def show_menu(self):
        self.frame_create_player.pack_forget()
        self.frame_buttons.pack(expand=True)

    def show_select_player(self):
        self.frame_buttons.pack_forget()
        self.frame_select_player.pack(expand=True, fill="both")

    def select_player_save(self):
        selected = self.listbox.get(self.listbox.curselection())
        mb.showinfo("Gewählt",selected)

    def show_menu_1(self):
        self.frame_select_player.pack_forget()
        self.frame_buttons.pack(expand=True)

    def play(self):
        print("play")
    def score(self):
        print("score")
    def exit_game(self):
        self.root.destroy()

init_db()
snake_game()