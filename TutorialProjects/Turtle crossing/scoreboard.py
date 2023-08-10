from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def current_level(self, level_number):
        self.clear()
        # self.level = level_number
        self.write(f"Level = {level_number}", font=FONT)

    # def level_increase(self):
    #     self.LEVEL += 1