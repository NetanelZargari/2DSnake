import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-150, -100, -50, 0, 50, 100]
turtlim = []
is_race_on = False


for n in range(len(colors)):
    new_trtl = Turtle(shape="turtle")
    new_trtl.color(colors[n])
    new_trtl.penup()
    new_trtl.goto(x=-240, y=y_pos[n])
    turtlim.append(new_trtl)

if user_bet:
    is_race_on = True

while is_race_on:
    for tlt in turtlim:
        if tlt.xcor() > 230:
            is_race_on = False
            winner = tlt.pencolor()
            if winner == user_bet:
                print("You win!")
            else:
                print("You lose!")

        rand_dis = random.randint(0, 10)
        tlt.forward(rand_dis)


screen.exitonclick()
