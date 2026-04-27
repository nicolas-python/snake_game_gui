import tkinter as tk

direction = None
x = 200
y = 200
canvas = None
snake_part = None

#zuweisung der tasten event = funktion wird nur ausgeführt, wenn dieses Event passiert
def go_left(event):
    global direction
    direction = "left"

def go_right(event):
    global direction
    direction = "right"

def go_up(event):
    global direction
    direction = "up"

def go_down(event):
    global direction
    direction = "down"


def snake():
    global canvas, snake_part,x ,y
    root = tk.Tk()
    root.title("Snake Game")
    root.geometry("400x400")

    #Canvas = Zeichenfläche in Tkinter
    #Canvas = Spielfeld zum Zeichnen von Objekten (Snake, Food, etc.)
    canvas = tk.Canvas(root, width=400, height=400, bg="black")
    canvas.pack()

    #start position
    body_x = 200
    body_y = 200

    #schlange model
    snake_part = []
    head = canvas.create_rectangle(body_x, body_y, body_x + 20, body_y+ 20, fill = "red")
    snake_part.append(head)

    body = canvas.create_rectangle(body_x, body_y, body_x + 20, body_y + 20, fill="green")
    snake_part.append(body)

    root.bind("<space>", grow_snake)

    #steuerung (pfeiltasten)
    root.bind("<Left>", go_left)
    root.bind("<Right>", go_right)
    root.bind("<Up>", go_up)
    root.bind("<Down>", go_down)

    move_snake()
    root.mainloop()

def grow_snake(event):
    last = snake_part[-1]                       #-1 = letzes element der liste

    coords = canvas.coords(last)
    x1, y1, x2, y2 = coords

    new_part = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    snake_part.append(new_part)


#bewegung aktualisierung
def move_snake():
    global x, y, direction, canvas, snake_part

    step = 20

    # alte Position speichern
    old_positions = []
    for part in snake_part:
        old_positions.append(canvas.coords(part))

    if direction == "left":
        x -= step
    elif direction == "right":
        x += step
    elif direction == "up":
        y -= step
    elif direction == "down":
        y += step

    #kopf bewegen
    canvas.coords(snake_part[0], x, y, x + 20, y + 20)  #bewegung von kopf aus

    #körper nachziehen
    for i in range(1, len(snake_part)):
        px1, py1, px2, py2 = old_positions[i - 1]
        canvas.coords(snake_part[i],px1, py1,px1 + 20, py1 + 20)              #coords =ändere die Position

    #aktualisierung
    canvas.after(200, move_snake)

snake()