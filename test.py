from turtle import Turtle, Screen
import random

screen = Screen()

# screen.setup(width=600, height=600)

trtl = Turtle()
colors = ["black", "yellow", "blue", "green", "red", "DarkOrchid", "CornflowerBlue"]


def up():
    trtl.forward(20)


def down():
    trtl.backward(20)


def left():
    trtl.left(90)


def right():
    trtl.right(90)


screen.listen()


screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")

screen.exitonclick()