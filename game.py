import tkinter as tk
import tkinter.messagebox as mb
import random

from database import save_score
from difficulty import get_speed
from PIL import Image, ImageTk     # für canvas hintergrundebilder import
import colorsys                     #damit kan ich Farben zwischen verschiedenen Farbsystemen umwandeln
                                    #für HSV -> RGB Farbverläufe / dynamische Farben



class snake:
    def __init__(self,player_name, difficulty):
        self.difficulty = difficulty
        self.root = tk.Toplevel()    #toplevel= neues Fenster im selben Programm
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
        self.stop_move_snake = None
        self.stop_timer = None
        self.colors = ["red", "green", "yellow", "blue", "white", "orange", "purple", "brown", "pink", "gold", "silver", "gray", "purple"]
        self.player_name = player_name
        self.running = True
        self.score_multiplier = 1
        self.obstacles = []
        self.hue = 0                                #HSV= H=Hue(Farbton),S=Saturation(Sättigung),V=Value(Helligkeit)
        self.special_food = None
        self.special_food_type = None
        self.special_food_cooldown = 10
        self.setup_game()

    def setup_game(self):
        self.speed = get_speed(self.difficulty)

        if self.difficulty == "easy":
            self.score_multiplier = 1
        elif self.difficulty == "normal":
            self.score_multiplier = 1.5
            self.create_normal_obstacles()
        elif self.difficulty == "hard":
            self.score_multiplier = 2
            self.create_hard_obstacles()

        self.creat_ui()
        self.bind_keys()
        self.start_game()
        self.root.mainloop()

    #hindernisse
    def create_normal_obstacles(self):                              #oben links, mitte rechts, unten links
        self.obstacles = [
            (100, 80), (120, 80),
            (100, 100), (120, 100),

            (240, 180), (260, 180),
            (240, 200), (260, 200),

            (120, 280), (140, 280),
            (120, 300), (140, 300),
        ]

    def create_hard_obstacles(self):                               #oben links, oben rechts, unten links, unten rechts
        self.obstacles = [
            (80, 80), (100, 80), (120, 80),
            (80, 100), (100, 100), (120, 100),
            (80, 120), (100, 120), (120, 120),

            (260, 80), (280, 80), (300, 80),
            (260, 100), (280, 100), (300, 100),
            (260, 120), (280, 120), (300, 120),

            (80, 260), (100, 260), (120, 260),
            (80, 280), (100, 280), (120, 280),
            (80, 300), (100, 300), (120, 300),

            (260, 260), (280, 260), (300, 260),
            (260, 280), (280, 280), (300, 280),
            (260, 300), (280, 300), (300, 300),
        ]

    #Oberfläche
    def creat_ui(self):
        self.score_label = tk.Label(self.root, text="Score: 0 - Zeit: 0", fg="black", bg="white")
        self.score_label.pack()

        # Canvas = Zeichenfläche in Tkinter
        # Canvas = Spielfeld zum Zeichnen von Objekten (Snake, Food, etc.)
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

        if self.difficulty == "easy":
            bg_path = random.choice([
                "backgrounds/easy_gras.png",
                "backgrounds/easy_gras_2.png"])

        elif self.difficulty == "normal":
            bg_path = "backgrounds/normal_gras.png"
        elif self.difficulty == "hard":
            bg_path = "backgrounds/hard_lava.png"
        else:
            bg_path = "backgrounds/normal_gras.png"

        self.bg_image = Image.open(bg_path)
        self.bg_image = self.bg_image.resize((400, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        for obstacle in self.obstacles:
            x, y = obstacle

            self.canvas.create_rectangle(
                x,
                y,
                x + 20,
                y + 20,
                fill="gray"
            )

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

        self.spawn_special_food()

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

        if self.special_food_cooldown > 0:
            self.special_food_cooldown -= 1

        self.spawn_special_food()

        self.stop_timer = self.canvas.after(1000, self.update_timer)

    #essen
    def spawn_food(self):

        while True:
            food_x = random.randint(0, 18) * 20
            food_y = random.randint(0, 18) * 20

            if (food_x, food_y) in self.obstacles:
                continue

            collision_with_snake = False

            for part in self.snake_part:
                x1, y1, x2, y2 = self.canvas.coords(part)

                if (food_x, food_y) == (x1, y1):
                    collision_with_snake = True
                    break

            if collision_with_snake:
                continue

            break

        self.food = self.canvas.create_rectangle(food_x, food_y, food_x + 20, food_y + 20, fill="yellow")

    def spawn_special_food(self):
        if self.special_food is not None:
            return

        if self.special_food_cooldown > 0:
            return

        if random.random() > 0.1:
            return

        x = random.randint(0, 18) * 20
        y = random.randint(0, 18) * 20

        food_type = random.randint(1, 2)

        if food_type == 1:
            color = "blue"
            effect = "score"

        elif food_type == 2:
            color = "green"
            effect = "grow"

        elif food_type == 3:
            color = "Light blue"
            effect = "slow"

        elif food_type == 4:
            color ="light purple"
            effect = "poison"

        self.special_food_type = effect

        self.special_food = self.canvas.create_rectangle(x,y,x + 20,y + 20,fill=color)

        self.canvas.after(5000, self.remove_special_food)


    def remove_special_food(self):
        if self.special_food is not None:
            self.canvas.delete(self.special_food)
            self.special_food = None


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

        if self.special_food_collision():
            if self.special_food_type == "score":
                self.score += 3
                self.score_label.config(text=f"Score: {self.score} - Zeit: {self.game_timer}")

            elif self.special_food_type == "grow":
                self.grow_snake()

            elif self.special_food_type == "slow":
                self.speed += 50

            elif self.special_food_type == "poison":
                self.score -= 10
                self.posion_message()

            self.canvas.delete(self.special_food)
            self.special_food = None

        if self.collision():
            self.game_over()
            return

        # aktualisierung
        self.stop_move_snake = self.canvas.after(self.speed, self.move_snake)

    def posion_message(self):
        self.score_label.config(text=f"Score: {self.score} - Zeit: {self.game_timer}")

        msg = self.canvas.create_text(200, 200, text="-2 Punkte!", fill="hotpink", font=("Arial", 16, "bold"))

    def stop_all(self):
        if self.stop_move_snake is not None:
            self.canvas.after_cancel(self.stop_move_snake)
            self.stop_move_snake = None

        if self.stop_timer is not None:
            self.canvas.after_cancel(self.stop_timer)
            self.stop_timer = None

    #Kollision
    def collision(self):
        if not self.moved:
            return False

        head_coords = self.canvas.coords(self.snake_part[0])
        x1, y1, x2, y2 = head_coords

        #wand kollision
        if x1 < 0 or x1 >= 380 or y1 < 0 or y1 >= 380:  # 400-20=380 Snake ist 20px groß, letzter gültiger Startpunkt ist 380 sonst wäre der Kopf schon teilweise außerhalb, bevor die Kollision greift
            return True

        #kollesion mit sich selbst
        for part in self.snake_part[1:]:
            if self.canvas.coords(part) == head_coords:
                return True

        #hinderniss kollesion
        for ox, oy in self.obstacles:
            if (x1, y1) == (ox, oy):
                return True


        return False

    # vergleicht ob kopf und essen auf gleicher position sind
    def food_collision(self):
        if self.food is None :
            return False

        head_coords = self.canvas.coords(self.snake_part[0])
        return self.canvas.coords(self.food) == head_coords

    def special_food_collision(self):
        if self.special_food is None :
            return False

        head_coords = self.canvas.coords(self.snake_part[0])

        return self.canvas.coords(self.special_food) == head_coords


    def grow_snake(self):
        self.score += self.score_multiplier
        self.score_label.config(text=f"Score: {self.score} - Zeit: {self.game_timer}")
        last = self.snake_part[-1]  # -1 = letzes element der liste

        coords = self.canvas.coords(last)
        x1, y1, x2, y2 = coords

        new_part = self.canvas.create_rectangle(x1, y1, x2, y2, fill="dark green")
        self.snake_part.append(new_part)

        color = random.choice(self.colors)

        for part in self.snake_part[1:]:
            self.canvas.itemconfig(part, fill=color)

    #game over
    def game_over(self):
        self.running = False
        self.stop_all()
        save_score(self.player_name, self.score, self.game_timer)
        self.save_difficulty()

        self.game_over_text = self.canvas.create_text(200, 100, text="Game Over", fill="white",font=("Arial", 20, "bold"))  #font =bestimmt, wie der text aussieht (Schriftart, Größe, Stil)
        self.animate_text()

        answer = mb.askyesno("Nochmal spielen?", "Willst du direkt nochmal spielen?")

        if answer == True:
            self.reset_game()
            self.difficulty = self.load_difficulty()
            self.setup_game()

        else:
            self.canvas.delete("all")
            self.root.destroy()

    def save_difficulty(self):
        with open("settings.txt", "w") as f:
            f.write(self.difficulty)

    def load_difficulty(self):
        try:
            with open("settings.txt", "r") as f:
                return f.read()
        except:
            return "normal"

    def animate_text(self,i=0):

        self.hue += 0.02                    #farbwert erhöhen (langsamer Farbwechsel)

        if self.hue > 1:                    #hue geht wie ein kreis deswegen zurücksetzen
            self.hue = 0

        r, g, b = colorsys.hsv_to_rgb(self.hue, 1, 1)           #HSV=RGB umwandeln(1 = volle Sättigung & Helligkeit)

        color = f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"   #umrechnung in tkinter (RGB in Hex-Farben fur Tkinter

        self.canvas.itemconfig(self.game_over_text, fill=color)

        self.canvas.after(100, self.animate_text)

    def reset_game(self):
        self.canvas.destroy()                           #destroy = Canvas komplett entfernen
        self.score_label.destroy()                      #delete("all") → Inhalt löschen, Canvas bleibt

        self.x = 200
        self.y = 200
        self.score = 0
        self.game_timer = 0
        self.direction = None
        self.food = None
        self.snake_part = []
        self.moved = False
        self.running = True
