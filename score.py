from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("skyblue")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def gameOver(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", align=ALIGN, font=FONT)
