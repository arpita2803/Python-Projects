from turtle import Turtle
WIDTH = 5
LENGTH = 1


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=LENGTH, stretch_wid=WIDTH)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        x_pos = self.xcor()
        y_cor = self.ycor()
        self.goto(x_pos, y_cor + 20)

    def move_down(self):
        x_pos = self.xcor()
        y_cor = self.ycor()
        self.goto(x_pos, y_cor - 20)
