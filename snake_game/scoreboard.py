from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(-10, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score : {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
