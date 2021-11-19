import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name").title()
text = turtle.Turtle()

state = data["state"].tolist()

if answer_state in state:
    x_pos = int(data[data.state == answer_state].x)
    y_pos = int(data[data.state == answer_state].y)
    text.color("black")
    text.hideturtle()
    text.goto(x_pos, y_pos)
    text.write(answer_state, font=("Courier", 8, "normal"))


screen.mainloop()