import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another states name?")
    guess = str(answer_state).title()
    if guess == "Exit":
        not_guessed = [item for item in all_states if item not in correct_guess]
        # not_guessed = []
        # for item in all_states:
        #     if item not in correct_guess:
        #         not_guessed.append(item)
        states_to_learn = pd.DataFrame(data=not_guessed, columns=["State"])
        states_to_learn.to_csv("learn.csv")
        break
    if guess in correct_guess:
        print("Already Guessed!")
    else:
        if guess in all_states:
            correct_guess.append(guess)
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_data = states[states.state == guess]
            state_turtle.goto(float(state_data.x), float(state_data.y))
            state_turtle.write(guess, align='left', font=('Arial', 8, 'normal'))
        else:
            print("Incorrect Guess")

