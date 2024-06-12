from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race:"
                                                          " red, orange, yellow, green, blue, purple. Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

def_y = -100
all_turtle = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle])
    new_turtle.goto(x=-230, y=def_y)
    def_y += 30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
