import tkinter as tk
import sqlite3

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
    #erst datenbank öffnen
    conn = sqlite3.connect("snake.db")
    c= conn.cursor()
    #dan daten holen
    c.execute("SELECT name FROM players")
    players = c.fetchall()
    #dan in liste eintragen
    for p in players:
        listbox.insert(tk.END, p[0])

    conn.close()

    return listbox