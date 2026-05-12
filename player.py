import tkinter as tk
from database import get_players


def create_player(frame):
    label = tk.Label(frame,text="Spielername:",bg="cyan")
    label.pack(pady=(20, 5))

    entry = tk.Entry(frame, bg="grey", fg="black")
    entry.pack(pady=10)

    return entry

def select_player(frame):

    label = tk.Label(frame, text="Spielername auswählen:", bg="cyan")
    label.pack(pady=10)

    listbox = tk.Listbox(frame, bg="grey", fg="black")
    listbox.pack(pady=10)

    players = get_players()

    #in liste eintragen
    for p in players:
        listbox.insert(tk.END, p[0])

    return listbox