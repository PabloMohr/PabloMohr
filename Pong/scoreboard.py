from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update_score(self.score)


    def update_score(self, points):
        self.clear()
        self.score += points
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)



