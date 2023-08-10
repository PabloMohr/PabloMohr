import turtle
import pandas

data = pandas.read_csv("50_states.csv")
game_is_on = True


def write_state():
    ALIGNMENT = "center"
    FONT = ("Courier", 10, "normal")
    state_turtle = turtle.Turtle()
    data_coords = data[data.state == f"{answer_state}"]
    x_coord = int(data_coords.x.iloc[0])
    y_coord = int(data_coords.y.iloc[0])
    state_turtle.penup()
    state_turtle.goto(x_coord, y_coord)
    state_turtle.hideturtle()
    state_turtle.write(answer_state, align=ALIGNMENT, font=FONT)


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
points = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{points}/50 States correct", prompt="What's another state's name?").title()
    turtle.clear()
    if answer_state in data.state.tolist():
        if answer_state in correct_guesses:
            turtle.write("You already have guessed that state", align="center", font=("Courier", 26, "bold"))
            print("You already guessed that state")
        else:
            correct_guesses.append(answer_state)
            points += 1
            write_state()
        if points == 50:
            turtle.write("GAME OVER", align="center", font=("Courier", 34, "bold"))
            game_is_on = False

    else:
        turtle.write("That's not a state", align="center", font=("Courier", 30, "bold"))
        print("That's not a state")

screen.exitonclick()
