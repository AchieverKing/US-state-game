import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
total_guess = 50
data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()

while len(guessed_states) < total_guess:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_guess}Guess the State",
                                    prompt="What's another state name?")
    guess = answer_state.title()
    if guess == "Exit":
        learn_state = [states for states in state_list if states not in guessed_states]
        learn = pandas.DataFrame(learn_state)
        learn.to_csv("learn_states.csv")
        break
    if guess in state_list:
        guessed_states.append(guess)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == guess]
        tim.goto(x=int(state_data.x), y=int(state_data.y))
        tim.write(guess)


# def get_mouse_click_cor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_cor)


# turtle.mainloop()
