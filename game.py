import tkinter as tk
import tkinter.messagebox as mb
import random


class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.root.geometry("400x400")

        self.direction = None
        self.x = 200
        self.y = 200
        self.canvas = None
        self.snake_part = []
        self.moved = False
        self.food = None
        self.score = 0
        self.score_label = None
        self.game_timer = 0
        self.speed = 200
        self.pause = False

        self.setup_game()

    def setup_game(self):
        self.creat_ui()
        self.bind_keys()
        self.start_game()
        self.root.mainloop()

    #Oberfläche
    def creat_ui(self):
        self.score_label = tk.Label(self.root, text="Score: 0 - Zeit: 0", fg="black", bg="white")
        self.score_label.pack()

        # Canvas = Zeichenfläche in Tkinter
        # Canvas = Spielfeld zum Zeichnen von Objekten (Snake, Food, etc.)
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

    # steuerung
    def bind_keys(self):
        self.root.bind("<Left>", self.go_left)
        self.root.bind("<Right>", self.go_right)
        self.root.bind("<Up>", self.go_up)
        self.root.bind("<Down>", self.go_down)
        self.root.bind("<p>", self.pause_game)

    #start game
    def start_game(self):
        self.snake()
        self.spawn_food()
        self.update_timer()
        self.move_snake()

    #bedienung
    #zuweisung der tasten event = funktion wird nur ausgeführt, wenn dieses Event passiert
    def go_left(self,event):
        self.direction = "left"

    def go_right(self,event):
        self.direction = "right"

    def go_up(self,event):
        self.direction = "up"

    def go_down(self,event):
        self.direction = "down"

    def pause_game(self,event):
        self.pause = not self.pause

    #schlange model
    def snake(self):
        self.root.bind("<p>", self.pause_game)
        #start position
        body_x = 200
        body_y = 200

        self.snake_part = []
        head = self.canvas.create_rectangle(body_x, body_y, body_x + 20, body_y+ 20, fill = "red")
        self.snake_part.append(head)

        body = self.canvas.create_rectangle(body_x, body_y, body_x + 20, body_y + 20, fill="green")
        self.canvas.itemconfig(body, state="hidden")
        self.snake_part.append(body)

    #Zeit
    def update_timer(self):

        if self.pause:
            self.canvas.after(1000, self.update_timer)
            return

        self.game_timer += 1
        self.score_label.config(text=f"Score: {self.score} - Zeit: {self.game_timer}")

        if self.game_timer % 10 == 0:    #% = Modulo → berechnet den Rest einer Division wen rest 0 -10 wen rest vorhanden geschwindigkeit gleich
            self.speed -=10

        self.canvas.after(1000, self.update_timer)

    #essen
    def spawn_food(self):

        food_x = random.randint(0, 19) * 20
        food_y = random.randint(0, 19) * 20

        self.food = self.canvas.create_rectangle(food_x, food_y, food_x + 20, food_y + 20, fill="yellow")

    #bewegung aktualisierung

    def move_snake(self):
        if self.pause:
            self.canvas.after(200, self.move_snake)
            return

        if self.direction is not None:
            self.moved = True

        # Körper sichtbar machen beim ersten Move
        if self.canvas.itemcget(self.snake_part[1], "state") == "hidden" and self.direction is not None:
            self.canvas.itemconfig(self.snake_part[1], state="normal")

        step = 20

        # alte Position speichern
        old_positions = []
        for part in self.snake_part:
            old_positions.append(self.canvas.coords(part))

        if self.direction == "left":
            self.x -= step
        elif self.direction == "right":
            self.x += step
        elif self.direction == "up":
            self.y -= step
        elif self.direction == "down":
            self.y += step

        # kopf bewegen
        self.canvas.coords(self.snake_part[0], self.x, self.y, self.x + 20, self.y + 20)  # bewegung von kopf aus

        # körper nachziehen
        for i in range(1, len(self.snake_part)):
            px1, py1, px2, py2 = old_positions[i - 1]
            self.canvas.coords(self.snake_part[i], px1, py1, px1 + 20, py1 + 20)  # coords =ändere die Position

        if self.food_collision():
            self.canvas.delete(self.food)
            self.food = None  # reset food, sonst coords() error (da canvas.delete nur objekt löscht nicht die Variable auf None setzt
            self.grow_snake()
            self.spawn_food()

        if self.collision():
            self.game_over()
            return

        # aktualisierung
        self.canvas.after(self.speed, self.move_snake)

    #Kollision
    def collision(self):

        if not self.moved:
            return False

        head_coords = self.canvas.coords(self.snake_part[0])
        x1, y1, x2, y2 = head_coords

        if x1 < 0 or x1 >= 380 or y1 < 0 or y1 >= 380:  # 400-20=380 Snake ist 20px groß, letzter gültiger Startpunkt ist 380 sonst wäre der Kopf schon teilweise außerhalb, bevor die Kollision greift
            return True

        for part in self.snake_part[1:]:
            if self.canvas.coords(part) == head_coords:
                return True

        return False

    # vergleicht ob kopf und essen auf gleicher position sind
    def food_collision(self):
        if self.food is None :
            return False

        head_coords = self.canvas.coords(self.snake_part[0])
        return self.canvas.coords(self.food) == head_coords

    def grow_snake(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score} - Zeit: {self.game_timer}")
        last = self.snake_part[-1]  # -1 = letzes element der liste

        coords = self.canvas.coords(last)
        x1, y1, x2, y2 = coords

        new_part = self.canvas.create_rectangle(x1, y1, x2, y2, fill="dark green")
        self.snake_part.append(new_part)

    #game over
    def game_over(self):

        mb.showinfo("Game Over","Game Over!")

        answer = mb.askyesno("Nochmal spielen?", "Willst du direkt nochmal spielen?")

        if answer == True:
            self.reset_game()
            self.move_snake()
            self.update_timer()
            self.spawn_food()

        else:
            self.canvas.delete("all")
            self.root.destroy()

    def reset_game(self):
        self.canvas.delete("all")

        self.x = 200
        self.y = 200
        self.score = 0
        self.game_timer = 0
        self.direction = None
        self.food = None
        self.snake_part = []

game = SnakeGame()