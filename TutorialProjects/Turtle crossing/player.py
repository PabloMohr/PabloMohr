from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def go_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def turn_right(self):
        self.setheading(0)
        x_move = self.xcor() + MOVE_DISTANCE
        self.goto(x_move, self.ycor())

    def turn_left(self):
        self.setheading(180)
        x_move = self.xcor() - MOVE_DISTANCE
        self.goto(x_move, self.ycor())

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False