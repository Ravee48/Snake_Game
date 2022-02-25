from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        # self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increased_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)