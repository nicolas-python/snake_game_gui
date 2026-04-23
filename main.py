#snake

import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

from player import create_player as cp
from player import select_player as sp
from database import init_db
from database import save_player
from game import snake

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

        self.clear_button_select = tk.Button(self.frame_select_player,text="Auswahl löschen",command=self.delete_player)
        self.clear_button_select.pack(pady=10)

        self.back_button_select = tk.Button(self.frame_select_player, text="Zurück", command=self.show_menu_1)
        self.back_button_select.pack(pady=10)

        self.root.mainloop()

    def create_player_save(self):
        name = self.entry.get()
        save_player(name)

        self.reload_players()

    def reload_players(self):
        self.listbox.delete(0, tk.END)
        conn = sqlite3.connect("snake.db")
        c = conn.cursor()

        c.execute("SELECT name FROM players")
        players = c.fetchall()

        for p in players:
            self.listbox.insert(tk.END, p[0])

        conn.close()

    def show_create_player(self):
        self.frame_buttons.pack_forget()
        self.frame_create_player.pack(expand=True, fill="both")
    #zurück creatplayer auswahl
    def show_menu(self):
        self.frame_create_player.pack_forget()
        self.frame_buttons.pack(expand=True)

    def show_select_player(self):
        self.frame_buttons.pack_forget()
        self.frame_select_player.pack(expand=True, fill="both")

    def select_player_save(self):
        selected = self.listbox.get(self.listbox.curselection())
        mb.showinfo("Gewählt",selected)
    #zurück player auswahl
    def show_menu_1(self):
        self.frame_select_player.pack_forget()
        self.frame_buttons.pack(expand=True)

    def delete_player(self):
        selected = self.listbox.get(tk.ACTIVE)

        if not selected:
            mb.showwarning("Fehler", "Bitte Spieler auswählen")
            return

        conn = sqlite3.connect("snake.db")
        c = conn.cursor()

        c.execute("DELETE FROM players WHERE name = ?", (selected,))
        conn.commit()
        conn.close()

        self.reload_players()

    def play(self):
        snake()

    def score(self):
        self.frame_button.pack_forget()
        self.score()

    def score(self):
        self.frame_buttons.pack_forget()
        self.frame_score = tk.Frame(self.root)
        self.frame_score.pack(expand=True, fill="both")

        label = tk.Label(self.frame_score, text="Score:")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self.frame_score, width=25)
        self.listbox.pack(pady=10)

        conn = sqlite3.connect("snake.db")
        c = conn.cursor()

        c.execute("SELECT name, score FROM players")
        scores = c.fetchall()

        for s in scores:
            self.listbox.insert(tk.END, f"{s[0]} - {s[1]} Punkte")

        conn.close()

        button_back = tk.Button(self.frame_score,text="Zurück",command=self.back_to_menu_2)
        button_back.pack(pady=10)

    #zurück score-menü
    def back_to_menu_2(self):
        self.frame_score.pack_forget()
        self.frame_buttons.pack(expand=True)

    def exit_game(self):
        self.root.destroy()

init_db()
snake_game()