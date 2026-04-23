import tkinter as tk

def snake():
    root = tk.Tk()
    root.title("Snake Game")
    root.geometry("400x400")

    # Canvas = Zeichenfläche in Tkinter
    # Canvas = Spielfeld zum Zeichnen von Objekten (Snake, Food, etc.)
    canvas = tk.Canvas(root, width=400, height=400, bg="black")
    canvas.pack()

    #schlange model
    canvas.create_rectangle(190, 190, 210, 210, fill="green")

    #map

    #steuerung (pfeiltasten)

    root.mainloop()
