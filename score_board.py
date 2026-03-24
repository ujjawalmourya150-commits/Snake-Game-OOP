from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score}  HIGHSCORE:{self.highscore}",align="center",font=("Courier",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.update_score()
    def reset_score(self):
        if self.score > self.highscore :
            with open("data.txt") as data:
                self.highscore = self.score
                with open("data.txt",mode="w") as data:
                    data.write(f"{self.highscore}")

            self.score = 0
        self.update_score()
