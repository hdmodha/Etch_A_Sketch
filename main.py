from turtle import Turtle, Screen
import random

screen = Screen()
is_game_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_cor = -100

for e in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(e)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_cor)
    y_cor += 45
    turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!! The {winning_color} turtle is the winner. ")
            else:
                print(f"You lost, The {winning_color} turtle is the winner. ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()


# screen.listen()
#
#
# def move_forward():
#     timmy.forward(20)
#
#
# def turn_right():
#     timmy.right(20)
#
#
# def turn_left():
#     timmy.left(20)
#
#
# def move_backward():
#     timmy.backward(20)
#
#
# def clear_drawing():
#     timmy.clear()
#     timmy.reset()
#
#
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=clear_drawing, key="c")

