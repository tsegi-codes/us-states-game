import turtle

import pandas

import time

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()

guessed_states = []
incorrect_count = 0

game_over = False

while not game_over:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in state_list:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        print(guessed_states)
        # print("correct answer")
        states = data[data.state == answer_state]
        states_x = states.x.item()
        states_y = states.y.item()

        writer.goto(states_x, states_y)
        writer.write(answer_state, align="center", font=("Arial", 10, "normal"))
    else:
        incorrect_count += 1
        print(incorrect_count)
    if incorrect_count >= 5 or answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_over = True
        writer.color("red")
        writer.goto(0, 0)
        writer.write("Game Over!! Try Again.", align="center", font=("Arial", 24, "normal"))
        time.sleep(0.9)

    if len(guessed_states) == 50:
        game_over = True
        writer.color("green")
        writer.goto(0,0)
        writer.write("You Got All!!", align="center", font=("Arial", 24, "normal"))



