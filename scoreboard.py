from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)