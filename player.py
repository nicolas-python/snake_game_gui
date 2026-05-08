import tkinter as tk
from database import get_players


def create_player(frame):
    label = tk.Label(frame,text="Spielername:")
    label.pack(pady=(20, 5))

    entry = tk.Entry(frame)
    entry.pack(pady=10)

    return entry

def select_player(frame):

    label = tk.Label(frame, text="Spielername auswählen:")
    label.pack(pady=10)

    listbox = tk.Listbox(frame)
    listbox.pack(pady=10)

    players = get_players()

    #in liste eintragen
    for p in players:
        listbox.insert(tk.END, p[0])

    return listbox