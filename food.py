import random
from turtle import Turtle

COLOR = ["red", "green", "yellow", "purple", "orange"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.random_color()
        self.speed("fastest")
        self.refresh()

    def random_color(self):
        self.color(random.choice(COLOR))
        self.random_head()

    def random_head(self):
        self.setheading(random.randint(0, 360))

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
