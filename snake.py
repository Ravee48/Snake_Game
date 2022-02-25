
import random
from turtle import Turtle
i = 0
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLOR = ["red", "green", "yellow", "purple", "orange"]

class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)

    def add_turtle(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        tim.speed("fastest")
        self.all_turtle.append(tim)

    def extend(self):
        self.add_turtle(self.all_turtle[-1].position())

    def move(self):
        for turtle in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[turtle - 1].xcor()
            new_y = self.all_turtle[turtle - 1].ycor()
            self.all_turtle[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
