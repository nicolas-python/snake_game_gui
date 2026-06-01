#snake
import tkinter as tk
import tkinter.messagebox as mb

from database import get_players
from database import delete_player
from database import save_player
from database import get_scores

from player import create_player as cp
from player import select_player as sp
from database import init_db
from database import get_highscores
from game import snake
from PIL import Image,ImageTk

class snake_game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#93c433")                     #configure= Widget-Eigenschaften ändern statt ersetzen

        # Background laden
        self.bg_image = Image.open("backgrounds/menu.png")
        self.bg_image = self.bg_image.resize((400, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Background Label
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)              #place da es im hintergrund bleiben soll knöpfe liegen drüber

        #menü
        self.frame_buttons = tk.Frame(self.root,bg="#93c433")
        self.frame_buttons.pack(expand=True)

        self.button_create_player = tk.Button(self.frame_buttons, text="Spieler erstellen",command=self.show_create_player, bg="cyan", activebackground="cyan" )
        self.button_create_player.pack(pady=10)

        self.button_select_player = tk.Button(self.frame_buttons, text="Spieler wählen",command=self.show_select_player, bg="cyan", activebackground="cyan")
        self.button_select_player.pack(pady=10)

        self.button_play = tk.Button(self.frame_buttons, text="Spielen", command=self.show_difficulty, bg="lime green", activebackground="lime green")
        self.button_play.pack(pady=10)

        self.button_score = tk.Button(self.frame_buttons, text="Score anzeigen", command=self.score, bg="cyan", activebackground="cyan")
        self.button_score.pack(pady=10)

        self.button_exit = tk.Button(self.frame_buttons, text="Beenden", command=self.exit_game, bg="cyan", activebackground="cyan")
        self.button_exit.pack(pady=10)

        #creat player
        self.frame_create_player = tk.Frame(self.root, bg="#93c433")
        self.entry = cp(self.frame_create_player)

        self.back_button_create = tk.Button(self.frame_create_player, text="Zurück", command=self.show_menu, bg="cyan", activebackground="cyan")
        self.back_button_create.pack(pady=10)

        self.save_button_create = tk.Button(self.frame_create_player,text="Speichern",command=self.create_player_save, bg="cyan", activebackground="green")
        self.save_button_create.pack(pady=10)

        #select player
        self.frame_select_player = tk.Frame(self.root, bg ="#93c433")
        self.player_listbox = sp(self.frame_select_player)

        self.save_button_select = tk.Button(self.frame_select_player, text="Auswählen", command=self.select_player_save, bg="cyan", activebackground="green")
        self.save_button_select.pack(pady=10)

        self.clear_button_select = tk.Button(self.frame_select_player,text="Auswahl löschen",command=self.delete_player, bg="cyan", activebackground="red")
        self.clear_button_select.pack(pady=10)

        self.back_button_select = tk.Button(self.frame_select_player, text="Zurück", command=self.show_menu, bg="cyan", activebackground="cyan")
        self.back_button_select.pack(pady=10)

        #select difficulty
        self.difficulty = "normal"
        self.frame_difficulty = tk.Frame(self.root, bg="#93c433")

        tk.Button(self.frame_difficulty,text="Easy",command=lambda: self.play("easy"), bg="cyan", activebackground="cyan").pack(pady=10)
        tk.Button(self.frame_difficulty, text="Normal", command=lambda: self.play("normal"), bg="cyan",activebackground="cyan").pack(pady=10)
        tk.Button(self.frame_difficulty, text="Hard", command=lambda: self.play("hard"), bg="cyan",activebackground="cyan").pack(pady=10)

        self.button_back_difficulty = tk.Button(self.frame_difficulty,text="Zurück",command=self.show_menu, bg="cyan",activebackground="cyan")
        self.button_back_difficulty.pack(pady=10)

        self.root.mainloop()

    def show_difficulty(self):
        self.frame_buttons.pack_forget()
        self.frame_difficulty.pack(expand=True, fill="both")

    def show_menu(self):

        self.frame_create_player.pack_forget()
        self.frame_select_player.pack_forget()
        self.frame_difficulty.pack_forget()

        if hasattr(self, "frame_score"):                #ausführen wenn es existiert sonst crash weil frame_score noch nicht erstellt wurde
            self.frame_score.pack_forget()

        self.frame_buttons.pack(expand=True)

    def create_player_save(self):
        name = self.entry.get()
        save_player(name)
        mb.showinfo("Spieler Erstellt", name)

        self.reload_players()

    def reload_players(self):
        self.player_listbox.delete(0, tk.END)

        players = get_players()

        for p in players:
            self.player_listbox.insert(tk.END, p[0])

    def show_create_player(self):
        self.frame_buttons.pack_forget()
        self.frame_create_player.pack(expand=True, fill="both")

    def show_select_player(self):
        self.frame_buttons.pack_forget()
        self.frame_select_player.pack(expand=True, fill="both")

    def select_player_save(self):
        selection =self.player_listbox.curselection()

        if not selection:
            mb.showwarning("Fehler","Bitte Spieler auswählen")
            return

        selected =self.player_listbox.get(selection[0])
        mb.showinfo("Gewählt", f"Du hast den Spieler {selected} gewählt")

    def delete_player(self):
        selected = self.player_listbox.get(tk.ACTIVE)

        if not selected:
            mb.showwarning("Fehler", "Bitte Spieler auswählen")
            return

        delete_player(selected)
        self.reload_players()

    def play(self, difficulty):
        self.difficulty = difficulty
        selection = self.player_listbox.curselection()                         #erste Zeile ausgewählt anzeige =(0,

        if not selection:
            mb.showwarning("Fehler","Bitte Spieler Wählen")
            return

        selected = self.player_listbox.get(selection[0])                           #holt richtigen werd also "name"
        snake(selected, self.difficulty)

    def score(self):
        self.frame_buttons.pack_forget()

        self.frame_score = tk.Frame(self.root, bg ="#93c433")
        self.frame_score.pack(expand=True, fill="both")

        highscore = get_highscores()

        for i, (name, score, game_timer) in enumerate(
                highscore):  # enumerate= liefert Index + Wert aus einer Liste (z.B. für Nummerierungen)
            text = f"{i + 1} - {name} - {score} Punkte - {game_timer} Sekunden"
            tk.Label(self.frame_score, text=text, bg="#93c433").pack(pady=10)

        label = tk.Label(self.frame_score, text="Score:",bg="#93c433")
        label.pack(pady=10)

        self.score_listbox = tk.Listbox(self.frame_score, width=25, bg="grey")
        self.score_listbox.pack(pady=10)

        scores = get_scores()

        for s in scores:
            self.score_listbox.insert(tk.END, f"{s[0]} - {s[1]} Punkte - {s[2]} Sekunden")

        button_back = tk.Button(self.frame_score,text="Zurück",command=self.show_menu,bg="cyan", activebackground="cyan")
        button_back.pack(pady=10)

    def exit_game(self):
        self.root.destroy()

init_db()
snake_game()