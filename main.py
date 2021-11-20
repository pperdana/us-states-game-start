import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
text = turtle.Turtle()
text.color("black")
text.hideturtle()
text.penup()


# record the correct and missing state
correct_states = []
miss_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What is another state's name").title()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in correct_states:
        x_pos = int(data[data.state == answer_state].x)
        y_pos = int(data[data.state == answer_state].y)
        text.goto(x_pos, y_pos)
        text.write(answer_state, font=("Courier", 8, "normal"))

        correct_states.append(answer_state)

miss_states = [state for state in states if state not in correct_states]

s = pandas.Series(miss_states)
s.to_csv("Missing states.csv")

# print(correct_list)
