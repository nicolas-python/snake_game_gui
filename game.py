import tkinter as tk
import tkinter.messagebox as mb
import random

direction = None
x = 200
y = 200
canvas = None
snake_part = None
moved = False
food = None

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
    canvas.itemconfig(body, state="hidden")
    snake_part.append(body)

    #steuerung (pfeiltasten)
    root.bind("<Left>", go_left)
    root.bind("<Right>", go_right)
    root.bind("<Up>", go_up)
    root.bind("<Down>", go_down)

    move_snake()
    spawn_food()
    root.mainloop()

def grow_snake():
    last = snake_part[-1]                       #-1 = letzes element der liste

    coords = canvas.coords(last)
    x1, y1, x2, y2 = coords

    new_part = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    snake_part.append(new_part)

def spawn_food():
    global food

    food_x = random.randint(1,19) * 20
    food_y = random.randint(1,19) * 20

    food = canvas.create_rectangle(food_x, food_y, food_x + 20, food_y + 20, fill="yellow")

#bewegung aktualisierung
def move_snake():
    global x, y, direction, canvas, snake_part, moved, food

    if direction is not None:
        moved = True

    # Körper sichtbar machen beim ersten Move
    if canvas.itemcget(snake_part[1], "state") == "hidden" and direction is not None:
        canvas.itemconfig(snake_part[1], state="normal")

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

    if food_collision():
        canvas.delete(food)
        food = None                                                 #reset food, sonst coords() error (da canvas.delete nur objekt löscht nicht die Variable auf None setzt
        grow_snake()
        spawn_food()

    if collision():
        game_over()
        return

    #aktualisierung
    canvas.after(200, move_snake)

def collision():
    if not moved:
        return False

    head_coords = canvas.coords(snake_part[0])

    for part in snake_part[1:]:
        if canvas.coords(part) == head_coords:
            return True

    return False

# vergleicht ob kopf und essen auf gleicher position sind
def food_collision():
    global food

    if food is None :
        return False

    head_coords = canvas.coords(snake_part[0])

    return canvas.coords(food) == head_coords


def game_over():
    global canvas

    mb.showinfo("Game Over","Game Over!")
    canvas.delete("all")

snake()