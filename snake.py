from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for pos in STARTING_POS:
            new_part = Turtle("square")
            new_part.color("yellow")
            new_part.penup()
            new_part.goto(pos)
            self.snake_parts.append(new_part)

    def add_parts(self, position):
        new_part = Turtle("square")
        new_part.color("yellow")
        new_part.penup()
        new_part.goto(position)
        self.snake_parts.append(new_part)

    def snake_bigger(self):
        self.add_parts(self.snake_parts[-1].position())

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_reset(self):
        for seg in self.snake_parts:
            seg.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

