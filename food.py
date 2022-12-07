from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x_rand = random.randint(-280, 280)
        y_rand = random.randint(-280, 280)
        self.goto(x_rand, y_rand)
