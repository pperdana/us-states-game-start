import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state = data["state"].tolist()
text = turtle.Turtle()
text.color("black")
text.hideturtle()
text.penup()


# record the correct state
correct_list = []

while len(correct_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_list)}/50 States Correct",
                                    prompt="What is another state's name").title()

    if answer_state in state and answer_state not in correct_list:
        x_pos = int(data[data.state == answer_state].x)
        y_pos = int(data[data.state == answer_state].y)
        text.goto(x_pos, y_pos)
        text.write(answer_state, font=("Courier", 8, "normal"))

        correct_list.append(answer_state)

# print(correct_list)
screen.mainloop()