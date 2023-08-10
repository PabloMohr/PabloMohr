from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto()