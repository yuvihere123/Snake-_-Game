from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")
GAME_OVER_FONT = ("Arial", 50, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 286)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=GAME_OVER_FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()
