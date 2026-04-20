import tkinter as tk

def create_player(frame):
    label = tk.Label(frame,text="Spielername:")
    label.pack(pady=(20, 5))

    entry = tk.Entry(frame)
    entry.pack(pady=(0, 20))